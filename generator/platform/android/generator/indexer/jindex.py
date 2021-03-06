#!/usr/bin/env python

# ORIGINAL SOURCE
#===- cindex.py - Python Indexing Library Bindings -----------*- python -*--===#
#
#                     The LLVM Compiler Infrastructure
#
# This file is distributed under the University of Illinois Open Source
# License. See LICENSE.TXT for details.
#
#===------------------------------------------------------------------------===#

# MODIFIED 
#
# 2/14/2013
# rvergis@zynga.com Added support for indexing Java classes 

from ctypes import *
import collections
import logging
import sys

def load_jindex_library(lib_name):
	# FIXME: It's probably not the case that the library is actually found in
	# this location. We need a better system of identifying and loading the
	# CIndex library. It could be on path or elsewhere, or versioned, etc.
	lib = None
	import platform
	name = platform.system()
	if name == 'Darwin':
		lib = cdll.LoadLibrary(lib_name + '.dylib')
	elif name == 'Windows':
		lib = cdll.LoadLibrary(lib_name + '.dll')
	else:
		lib = cdll.LoadLibrary(lib_name + '.so')
	return lib

# ctypes doesn't implicitly convert c_void_p to the appropriate wrapper
# object. This is a problem, because it means that from_parameter will see an
# integer and pass the wrong value on platforms where int != void*. Work around
# this by marshalling object arguments as void**.
c_object_p = POINTER(c_void_p)

lib_name = "libCXXGenerator"
lib = load_jindex_library(lib_name)

STR_ATTR_SIZE = 80
MAX_PACKAGE_COUNT = 256
MAX_CLASSE_COUNT = 1024

### Exception Classes ###

class TranslationUnitLoadError(Exception):
	pass

class TranslationUnitSaveError(Exception):
	pass

class CursorKind(object):

	_kinds = []
	_name_map = None

	def __init__(self, value):
		if value >= len(CursorKind._kinds):
			CursorKind._kinds += [None] * (value - len(CursorKind._kinds) + 1)
		if CursorKind._kinds[value] is not None:
			raise ValueError, "CursorKind already loaded"
		self.value = self._as_parameter_ = value
		CursorKind._kinds[value] = self
		CursorKind._name_map = None

	def from_param(self):
		return self.value

	@property
	def name(self):
		if self._name_map is None:
			self._name_map = {}
			for key,value in CursorKind.__dict__.items():
				if isinstance(value, CursorKind):
					self._name_map[value] = key
		return self._name_map[self]

	@property
	def id(self):
		return self.value

	@staticmethod
	def from_id(id):
		if id >= len(CursorKind._kinds) or CursorKind._kinds[id] is None:
			raise ValueError, "Unknown cursor kind"
		return CursorKind._kinds[id]

	@staticmethod
	def get_all_kinds():
		return filter(None, CursorKind._kinds)

	def __repr__(self):
		return 'CursorKind.%s' % (self.name,)


CursorKind.CLASS_DECL = CursorKind(4)
CursorKind.ENUM_DECL = CursorKind(5)
CursorKind.CONSTRUCTOR_DECL = CursorKind(7)
CursorKind.FUNCTION_DECL = CursorKind(8)
CursorKind.FIELD_DECL = CursorKind(74)
CursorKind.FIELD_TYPE_DECL = CursorKind(75)
CursorKind.RETURN_DECL = CursorKind(9)
CursorKind.PARAM_DECL = CursorKind(10)
CursorKind.CONSTRUCTOR = CursorKind(24)
CursorKind.DESTRUCTOR = CursorKind(25)
CursorKind.INVALID_FILE = CursorKind(70)
CursorKind.NO_DECL_FOUND = CursorKind(71)
CursorKind.NOT_IMPLEMENTED = CursorKind(72)
CursorKind.INVALID_CODE = CursorKind(73)

### Cursors ###

class Cursor(Structure):

	_fields_ = [
					("_kind_id", c_int),("_tu_id", c_longlong),
					("_str_attr_0", c_char_p),("_str_attr_1", c_char_p),("_str_attr_2", c_char_p),("_str_attr_3", c_char_p),
					("_int_attr_0", c_int),("_int_attr_1", c_int),("_int_attr_2", c_int),("_int_attr_3", c_int)
			   ]

	def from_result(res, fn, args):
		assert isinstance(res, Cursor)
		tu = None
		for arg in args:
			if isinstance(arg, TranslationUnit):
				tu = arg
				break

			if hasattr(arg, 'translation_unit'):
				tu = arg.translation_unit
				break

		assert tu is not None

		res._tu = tu
		return res

	def get_children(self):
		if not hasattr(self, '_children'):
			def visitor(child, parent, children):
				children.append(child)
				return 1
			children = []
			Cursor_visit(self, Cursor_visit_callback(visitor), children)
			self._children = children
		return self._children

	@property
	def kind(self):
		return CursorKind.from_id(self._kind_id)

	@property
	def str_attrs(self):
		if not hasattr(self, '_str_attrs'):
			self._update_attrs()
		return self._str_attrs

	@property
	def int_attrs(self):
		if not hasattr(self, '_int_attrs'):
			self._update_attrs()
		return self._int_attrs

	@property
	def displayname(self):
		if not hasattr(self, '_displayname'):
			self._displayname = Cursor_displayname(self)
		return self._displayname

	@property
	def description(self):
		if not hasattr(self, '_description'):
			self._description = Cursor_description(self)
		return self._description

	@property
	def type(self):
		if not hasattr(self, '_type'):
			self._type = Cursor_type(self)
		return self._type

	@property
	def translation_unit(self):
		if not hasattr(self, '_tu'):
			tu_id = Cursor_translationUnit(self)
			self._tu = TranslationUnit(tu_id)
		return self._tu

	@property
	def enum_values(self):
		def visitor(enum_value, enum_values):
			enum_values.append(enum_value)
			return 1
		enum_values = []
		Cursor_enum_values(self, self.type, Cursor_enum_values_callback(visitor), enum_values)
		return enum_values

	@property
	def parent_name(self):
		if not hasattr(self, '_parent_name'):
			self._parent_name = Cursor_parent_name(self)
		return self._parent_name

	def _update_attrs(self):
		if not hasattr(self, '_updated_attrs'):
			def visitor(int_attr, str_attr, attrs_holder):
				int_attrs = attrs_holder[0]
				int_attrs.append(int_attr)
				str_attrs = attrs_holder[1]
				str_attrs.append(str_attr)
			self._int_attrs = []
			self._str_attrs = []
			attrs_holder = [ self._int_attrs, self._str_attrs ]
			Cursor_visit_attrs(self, Cursor_visit_attrs_callback(visitor), attrs_holder)
			self._updated_attrs = True


class TypeKind(object):

	_kinds = []
	_name_map = None

	def __init__(self, value):
		if value >= len(TypeKind._kinds):
			TypeKind._kinds += [None] * (value - len(TypeKind._kinds) + 1)
		if TypeKind._kinds[value] is not None:
			raise ValueError,'TypeKind already loaded'
		self.value = value
		TypeKind._kinds[value] = self
		TypeKind._name_map = None

	def from_param(self):
		return self.value

	@property
	def name(self):
		if self._name_map is None:
			self._name_map = {}
			for key,value in TypeKind.__dict__.items():
				if isinstance(value,TypeKind):
					self._name_map[value] = key
		return self._name_map[self]

	@property
	def id(self):
		return self.value

	@staticmethod
	def from_id(id):
		if id >= len(TypeKind._kinds) or TypeKind._kinds[id] is None:
			raise ValueError,'Unknown type kind %d' % id
		return TypeKind._kinds[id]

	@staticmethod
	def from_name(name):
		for key,value in TypeKind.__dict__.items():
				if isinstance(value,TypeKind):
					return value
		return None

	def __repr__(self):
		return 'TypeKind.%s' % (self.name,)

TypeKind.UNKNOWN = TypeKind(0)
TypeKind.JAVA_INSTANCE = TypeKind(200)
TypeKind.JAVA_SINGLETON_FIELD = TypeKind(201)
TypeKind.JAVA_SINGLETON_ENUM_FIELD = TypeKind(215)
TypeKind.JAVA_NOT_INSTANTIATABLE = TypeKind(216)
TypeKind.JAVA_SINGLETON_INSTANCE = TypeKind(211)
TypeKind.JAVA_ENUM = TypeKind(202)
TypeKind.JAVA_ABSTRACT = TypeKind(203)
TypeKind.JAVA_STATIC_METHODS = TypeKind(204)
TypeKind.JAVA_PUBLIC_INSTANCE_METHOD = TypeKind(205)
TypeKind.JAVA_PUBLIC_STATIC_METHOD = TypeKind(206)
TypeKind.JAVA_PUBLIC_INSTANCE_FIELD = TypeKind(218)
TypeKind.JAVA_PUBLIC_STATIC_FIELD = TypeKind(217)
TypeKind.JAVA_PUBLIC_CONSTRUCTOR = TypeKind(207)
TypeKind.JAVA_PRIMITIVE = TypeKind(208)
TypeKind.JAVA_ARRAY = TypeKind(209)
TypeKind.JAVA_INTERFACE = TypeKind(210)
TypeKind.JAVA_TYPE_VARIABLE = TypeKind(212)
TypeKind.JAVA_GENERIC_ARRAY_TYPE = TypeKind(213)
TypeKind.WILDCARD_TYPE = TypeKind(214)
TypeKind.DUMMY = TypeKind(999)

class Type(Structure):

	_fields_ = [("_kind_id", c_int)]

	@property
	def kind(self):
		return TypeKind.from_id(self._kind_id)

	@property
	def translation_unit(self):
		return self._tu

	@staticmethod
	def from_result(res, fn, args):
		assert isinstance(res, Type)
		
		tu = None
		for arg in args:
			if hasattr(arg, 'translation_unit'):
				tu = arg.translation_unit
				break

		assert tu is not None
		res._tu = tu

		return res        

class JavaObject(object):
	def __init__(self, obj):
		assert isinstance(obj, c_object_p) and obj
		self.obj = self._as_parameter_ = obj

	def from_param(self):
		return self._as_parameter_

class TypeHierarchy(Structure):

	_fields_ = [
					("_type_id", c_longlong),
					("_child_count", c_int),
					("_type_name", c_char * STR_ATTR_SIZE),
					("_class_name", c_char * STR_ATTR_SIZE),
					("_package_name", c_char * STR_ATTR_SIZE),
			   ]

	def from_result(res, fn, args):
		assert isinstance(res, TypeHierarchy)
		return res

	def get_children(self):
		if not hasattr(self, '_children'):
			def visitor(child, parent, children):
				children.append(child)
				return 1
			children = list()
			TypeHierarchy_visit(self, TypeHierarchy_visit_callback(visitor), children)
			self._children = children
		return self._children

	@property
	def child_count(self):
		return self._child_count

	@property
	def type_name(self):
		if not hasattr(self, '_type_name_str'):
			chars = list()
			for ch in self._type_name:
				if ord(ch) == 0:
					break;
				else:
					chars.append(ch)
			self._type_name_str = "".join(chars)
		return self._type_name_str

	@property
	def class_name(self):
		if not hasattr(self, '_class_name_str'):
			chars = list()
			for ch in self._class_name:
				if ord(ch) == 0:
					break;
				else:
					chars.append(ch)
			self._class_name_str = "".join(chars)
		return self._class_name_str

	@property
	def package_name(self):
		if not hasattr(self, '_package_name_str'):
			chars = list()
			for ch in self._package_name:
				if ord(ch) == 0:
					break;
				else:
					chars.append(ch)
			self._package_name_str = "".join(chars)
		return self._package_name_str

	@classmethod
	def canCastClass1ToClass2(cls, clazz1_name, clazz2_name):
		c_types_clazz1_name = (c_char * STR_ATTR_SIZE)()
		c_types_clazz1_name.value = clazz1_name
		c_types_clazz2_name = (c_char * STR_ATTR_SIZE)()
		c_types_clazz2_name.value = clazz2_name
		return TypeHierarchy_canCastClass1ToClass2(c_types_clazz1_name, c_types_clazz2_name)

class Modifier(object):
	UNKNOWN = 0
	JAVA_PUBLIC = 1
	JAVA_STATIC = 8
	JAVA_FINAL = 16
	JAVA_INTERFACE = 512
	JAVA_ABSTRACT = 1024

	@classmethod
	def is_modifier(cls, modifiers, modifier):
		return modifiers & modifier == modifier

class PrimitiveType(object):

	_types_map = {}
	_name_map = None

	def __init__(self, value):
		if value in PrimitiveType._types_map:
			raise ValueError,'PrimitiveType already loaded'
		self.value = value
		PrimitiveType._types_map[value] = self
		PrimitiveType._name_map = None

	def from_param(self):
		return self.value

	@property
	def name(self):
		if self._name_map is None:
			self._name_map = {}
			for key,value in PrimitiveType.__dict__.items():
				if isinstance(value,PrimitiveType):
					self._name_map[value] = key
		return self._name_map[self]

	@property
	def id(self):
		return self.value

	@staticmethod
	def from_id(id):
		if id in PrimitiveType._types_map:
			return PrimitiveType._types_map[id]
		return None

	@staticmethod
	def is_primitive_id(id):
		return PrimitiveType.from_id(id) is not None

	@staticmethod
	def from_name(name):
		for key,value in PrimitiveType.__dict__.items():
				if isinstance(value,PrimitiveType):
					return value
		return None

	@staticmethod
	def is_primitive_name(name):
		return PrimitiveType.from_name(name) is not None

	def __repr__(self):
		return 'PrimitiveType.%s' % (self.name,)

PrimitiveType.BYTE = PrimitiveType("byte")
PrimitiveType.SHORT = PrimitiveType("short")
PrimitiveType.INT = PrimitiveType("int")
PrimitiveType.LONG = PrimitiveType("long")
PrimitiveType.FLOAT = PrimitiveType("float")
PrimitiveType.DOUBLE = PrimitiveType("double")
PrimitiveType.BOOLEAN = PrimitiveType("boolean")
PrimitiveType.CHAR = PrimitiveType("char")

class VoidType(object):

	_types_map = {}
	_name_map = None

	def __init__(self, value):
		if value in VoidType._types_map:
			raise ValueError,'VoidType already loaded'
		self.value = value
		VoidType._types_map[value] = self
		VoidType._name_map = None

	def from_param(self):
		return self.value

	@property
	def name(self):
		if self._name_map is None:
			self._name_map = {}
			for key,value in VoidType.__dict__.items():
				if isinstance(value,VoidType):
					self._name_map[value] = key
		return self._name_map[self]

	@property
	def id(self):
		return self.value

	@staticmethod
	def from_id(id):
		if id in VoidType._types_map:
			return VoidType._types_map[id]
		return None

	@staticmethod
	def is_void_id(id):
		return VoidType.from_id(id) is not None

	@staticmethod
	def from_name(name):
		for key,value in VoidType.__dict__.items():
				if isinstance(value,VoidType):
					return value
		return None

	@staticmethod
	def is_void_name(name):
		return VoidType.from_name(name) is not None

	def __repr__(self):
		return 'VoidType.%s' % (self.name,)

VoidType.VOID = VoidType("void")

class ArrayType(object):

	_types_map = {}
	_name_map = None

	def __init__(self, value):
		if value in ArrayType._types_map:
			raise ValueError,'ArrayType already loaded'
		self.value = value
		ArrayType._types_map[value] = self
		ArrayType._name_map = None

	def from_param(self):
		return self.value

	@property
	def name(self):
		if self._name_map is None:
			self._name_map = {}
			for key,value in ArrayType.__dict__.items():
				if isinstance(value,ArrayType):
					self._name_map[value] = key
		return self._name_map[self]

	@property
	def id(self):
		return self.value

	@staticmethod
	def from_id(id):
		if id in ArrayType._types_map:
			return ArrayType._types_map[id]
		return None

	@staticmethod
	def is_array_id(id):
		return ArrayType.from_id(id) is not None

	@staticmethod
	def from_name(name):
		for key,value in ArrayType.__dict__.items():
				if isinstance(value,ArrayType):
					return value
		return None

	@staticmethod
	def is_array_name(name):
		return ArrayType.from_name(name) is not None

	def __repr__(self):
		return 'ArrayType.%s' % (self.name,)

ArrayType.OBJECT_ARRAY = ArrayType("_object_array_type")		
ArrayType.BYTE_ARRAY = ArrayType("_byte_array_type")
ArrayType.SHORT_ARRAY = ArrayType("_short_array_type")
ArrayType.INT_ARRAY = ArrayType("_int_array_type")
ArrayType.LONG_ARRAY = ArrayType("_long_array_type")
ArrayType.FLOAT_ARRAY = ArrayType("_float_array_type")
ArrayType.DOUBLE_ARRAY = ArrayType("_double_array_type")
ArrayType.BOOLEAN_ARRAY = ArrayType("_boolean_array_type")
ArrayType.CHAR_ARRAY = ArrayType("_char_array_type")

class CallbackType(object):
	UNKNOWN = 0
	ENTER = 1
	PROCESS = 2
	EXIT = 4

class Index(JavaObject):

	@staticmethod
	def create(classpath):
		return Index(Index_create(create_string_buffer(classpath)))

	def parse(self, res):
		return TranslationUnit.from_source(res, self)

	def build_config_closure(self, config_data):
		return TranslationUnit.build_config_closure(config_data)

	@property
	def status(self):
		return Index_status()

	@property
	def statusMessage(self):
		return Index_statusMessage();

	@staticmethod
	def destroy():
		return Index_destroy()

class TranslationUnit(JavaObject):

	@classmethod
	def build_config_closure(cls, config_data):
		assert "packages" in config_data
		assert "classes" in config_data
		def visitor(callback_type, cursor_type, type, modifiers, name, idx, type_id, config_data_stack):
			TranslationUnit._process_config_data(callback_type, cursor_type, type, modifiers, name, idx, type_id, config_data_stack)
			return 0
		packages = config_data["packages"]
		classes = config_data["classes"]
		c_types_packages = ((c_char * STR_ATTR_SIZE) * MAX_PACKAGE_COUNT)()
		for idx in range(len(packages)):
			c_types_packages[idx].value = packages[idx]["name"]
		c_types_packages_count = len(packages)
		c_types_classes = ((c_char * STR_ATTR_SIZE) * MAX_CLASSE_COUNT)()
		for idx in range(len(classes)):
			c_types_classes[idx].value = classes[idx]["name"]
		c_types_classes_count = len(classes)
		config_data_stack = list()
		config_data_stack.append(config_data)
		TranslationUnit_classes_visit(c_types_packages, c_types_packages_count, c_types_classes, c_types_classes_count, TranslationUnit_classes_visit_callback(visitor), config_data_stack)
	
	@classmethod
	def from_source(cls, res, index):
		ptr = TranslationUnit_parse(index, res)
		if ptr is None:
			raise TranslationUnitLoadError("Error parsing translation unit")

		return cls(ptr)

	def __init__(self, ptr):
		JavaObject.__init__(self, ptr)

	def __del__(self):
		TranslationUnit_dispose(self)

	@property
	def cursor(self):
		return TranslationUnit_cursor(self)

	@classmethod
	def _process_config_data(cls, callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack):
		if CursorKind.from_id(cursor_type) == CursorKind.CLASS_DECL:
			TranslationUnit._process_class_config_data(callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack)
		if CursorKind.from_id(cursor_type) == CursorKind.CONSTRUCTOR_DECL:
			TranslationUnit._process_constructor_config_data(callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack)
		if CursorKind.from_id(cursor_type) == CursorKind.FUNCTION_DECL:
			TranslationUnit._process_function_config_data(callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack)
		if CursorKind.from_id(cursor_type) == CursorKind.FIELD_DECL:
			TranslationUnit._process_field_config_data(callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack)
		if CursorKind.from_id(cursor_type) == CursorKind.PARAM_DECL:
			TranslationUnit._process_param_config_data(callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack)
		if CursorKind.from_id(cursor_type) == CursorKind.RETURN_DECL:
			TranslationUnit._process_return_config_data(callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack)
		if CursorKind.from_id(cursor_type) == CursorKind.FIELD_TYPE_DECL:
			TranslationUnit._process_field_type_config_data(callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack)

	@classmethod
	def _process_class_config_data(cls, callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack):
		logging.debug("_process_class_config_data " + name) 
		if callback_type == CallbackType.ENTER:
			config_data = config_data_stack[0] # classes at the root
			config_data = TranslationUnit._find_or_create_class_config_data(config_data["classes"], name)
			config_data_stack.append(config_data)
		if callback_type == CallbackType.PROCESS:
			config_data = config_data_stack[len(config_data_stack)-1]
			TranslationUnit._update_class_config_data(config_data, _type, modifiers, idx)
		if callback_type == CallbackType.EXIT:
			config_data_stack.pop()

	@classmethod
	def _process_constructor_config_data(cls, callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack):
		logging.debug("_process_constructor_config_data " + name) 
		if callback_type == CallbackType.ENTER:
			config_data = config_data_stack[len(config_data_stack)-1]
			config_data = TranslationUnit._find_or_create_constructor_config_data(config_data["constructors"], name)
			config_data_stack.append(config_data)
		if callback_type == CallbackType.PROCESS:
			class_config_data = config_data_stack[len(config_data_stack)-2]
			config_data = config_data_stack[len(config_data_stack)-1]
			TranslationUnit._update_constructor_config_data(class_config_data, config_data, _type, modifiers, idx)
		if callback_type == CallbackType.EXIT:
			config_data_stack.pop()

	@classmethod
	def _process_function_config_data(cls, callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack):
		logging.debug("_process_function_config_data " + name) 
		if callback_type == CallbackType.ENTER:
			config_data = config_data_stack[len(config_data_stack)-1]
			config_data = TranslationUnit._find_or_create_function_config_data(config_data["functions"], name)
			config_data_stack.append(config_data)
		if callback_type == CallbackType.PROCESS:
			class_config_data = config_data_stack[len(config_data_stack)-2]
			config_data = config_data_stack[len(config_data_stack)-1]
			TranslationUnit._update_function_config_data(class_config_data, config_data, _type, modifiers, idx)
		if callback_type == CallbackType.EXIT:
			config_data_stack.pop()

	@classmethod
	def _process_field_config_data(cls, callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack):
		logging.debug("_process_field_config_data " + name)
		if callback_type == CallbackType.ENTER:
			config_data = config_data_stack[len(config_data_stack)-1]
			config_data = TranslationUnit._find_or_create_field_config_data(config_data["fields"], name)
			config_data_stack.append(config_data)
		if callback_type == CallbackType.PROCESS:
			class_config_data = config_data_stack[len(config_data_stack)-2]
			config_data = config_data_stack[len(config_data_stack)-1]
			TranslationUnit._update_field_config_data(class_config_data, config_data, _type, modifiers, idx)
		if callback_type == CallbackType.EXIT:
			config_data_stack.pop()

	@classmethod
	def _process_param_config_data(cls, callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack):
		logging.debug("_process_param_config_data " + name) 
		if callback_type == CallbackType.ENTER:
			config_data = config_data_stack[len(config_data_stack)-1]
			type_hierarchy = TranslationUnit._create_type_hierarchy(type_id)
			type_hierarchy_structure = TranslationUnit._build_type_hierarchy_structure(type_hierarchy)
			config_data = TranslationUnit._find_or_create_param_config_data(config_data["params"], type_hierarchy_structure)
			config_data_stack.append(config_data)
		if callback_type == CallbackType.PROCESS:
			#process
			pass
		if callback_type == CallbackType.EXIT:
			config_data_stack.pop()

	@classmethod
	def _process_return_config_data(cls, callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack):
		logging.debug("_process_return_config_data " + name) 
		if callback_type == CallbackType.ENTER:
			config_data = config_data_stack[len(config_data_stack)-1]
			type_hierarchy = TranslationUnit._create_type_hierarchy(type_id)
			type_hierarchy_structure = TranslationUnit._build_type_hierarchy_structure(type_hierarchy)
			config_data = TranslationUnit._find_or_create_return_config_data(config_data["returns"], type_hierarchy_structure)
			config_data_stack.append(config_data)
		if callback_type == CallbackType.PROCESS:
			#process
			pass
		if callback_type == CallbackType.EXIT:
			config_data_stack.pop()

	@classmethod
	def _process_field_type_config_data(cls, callback_type, cursor_type, _type, modifiers, name, idx, type_id, config_data_stack):
		logging.debug("_process_field_type_config_data " + name) 
		if callback_type == CallbackType.ENTER:
			config_data = config_data_stack[len(config_data_stack)-1]
			type_hierarchy = TranslationUnit._create_type_hierarchy(type_id)
			type_hierarchy_structure = TranslationUnit._build_type_hierarchy_structure(type_hierarchy)
			config_data = TranslationUnit._find_or_create_field_type_config_data(config_data, type_hierarchy_structure)
			config_data_stack.append(config_data)
		if callback_type == CallbackType.PROCESS:
			#process
			pass
		if callback_type == CallbackType.EXIT:
			config_data_stack.pop()

	@classmethod
	def _find_or_create_class_config_data(cls, classes, class_name):
		the_clazz = None
		for clazz in classes:
			if clazz["name"] == class_name:
				the_clazz = clazz
				break
		if not the_clazz:
			the_clazz = dict()
			classes.append(the_clazz)
		the_clazz["name"] = class_name
		the_clazz["constructors"] = the_clazz.get("constructors", list())
		the_clazz["functions"] = the_clazz.get("functions", list())
		the_clazz["fields"] = the_clazz.get("fields", list())
		return the_clazz

#   Special Class Tags
#		_enum 											Tag to indicate class should be enumerated
#		_interface											Tag to indicate class is an interface
#		_abstract											Tag to indicate class is abstract
#		_instance											Tag to indicate class instance should be created
#		_static 											Tag to indicate class has only static methods
#		_callback 											Tag to indicate class is a callback

	@classmethod
	def _update_class_config_data(cls, clazz, _type, modifiers, idx):
		if "tags" in clazz:
			tags = clazz["tags"]
		else:
			tags = list()

		tags = sorted(list(set(tags)))

		if "_no_proxy" in tags:
			tags = list()
			tags.append("_no_proxy")
		else:
			if Modifier.is_modifier(modifiers, Modifier.JAVA_FINAL):
				if '_callback' in tags:
					tags.remove('_callback')
				tags.append('_no_callback')
			type_kind = TypeKind.from_id(_type)
			if type_kind == TypeKind.JAVA_ENUM:
				tags[:] = list()
				tags.append("_enum")
			elif type_kind == TypeKind.JAVA_INTERFACE:
				tags[:] = list()
				tags.append("_interface")
			elif type_kind == TypeKind.JAVA_ABSTRACT:
				if "callback" in tags:
					tags[:] = list()
					tags.append("_callback")
				else:
					tags[:] = list()
				tags.append("_abstract")
			elif type_kind == TypeKind.JAVA_INSTANCE:
				if "callback" in tags:
					tags[:] = list()
					tags.append("_callback")
				else:
					tags[:] = list()
				tags.append("_instance")
			elif type_kind == TypeKind.JAVA_STATIC_METHODS:
				tags[:] = list()
				tags.append("_static")
			elif type_kind == TypeKind.JAVA_SINGLETON_INSTANCE:
				tags[:] = list()
				tags.append("_instance")
				tags.append("_singleton")
			elif type_kind == TypeKind.JAVA_SINGLETON_FIELD:
				tags[:] = list()
				tags.append("_instance")
				tags.append("_singleton")
			elif type_kind == TypeKind.JAVA_NOT_INSTANTIATABLE:
				tags[:] = list()
				tags.append("_abstract")
			if "_no_proxy" in tags:
				tags.remove("_no_proxy")
			tags.append("_proxy")

		tags = sorted(list(set(tags)))

		if len(tags) > 0:
			clazz["tags"] = tags
		else:
			if "tags" in clazz:
				del clazz["tags"]

	@classmethod
	def _update_constructor_config_data(cls, clazz, constructor, _type, modifiers, idx):
		if "tags" in constructor:
			tags = constructor["tags"]
		else:
			tags = list()

		tags = sorted(list(set(tags)))

		if "_no_proxy" in tags:
			tags = list()
			tags.append("_no_proxy")
		else:
			tags.append("_proxy")

		tags = sorted(list(set(tags)))
		if len(tags) > 0:
			constructor["tags"] = tags
		else:
			if "tags" in constructor:
				del constructor["tags"]

	@classmethod
	def _update_function_config_data(cls, clazz, function, _type, modifiers, idx):
		if "tags" in function:
			tags = function["tags"]
		else:
			tags = list()

		tags = sorted(list(set(tags)))

		if "_no_proxy" in tags:
			tags = list()
			tags.append("_no_proxy")
		else:
			if Modifier.is_modifier(modifiers, Modifier.JAVA_FINAL):
				if '_callback' in tags:
					tags.remove('_callback')
				tags.append('_no_callback')
			type_kind = TypeKind.from_id(_type)
			if type_kind == TypeKind.JAVA_PUBLIC_STATIC_METHOD:
				tags.append("_static")
				if "returns" in function:
					for retrn in function["returns"]:
						if retrn["type"] == clazz["name"]:
							if "children" not in retrn:
								tags.append("_singleton")
			elif type_kind == TypeKind.JAVA_PUBLIC_INSTANCE_METHOD:
				tags.append("_instance")
			if "_no_proxy" in tags:
				tags.remove("_no_proxy")
			tags.append("_proxy")

		tags = sorted(list(set(tags)))
		if len(tags) > 0:
			function["tags"] = tags
		else:
			if "tags" in function:
				del function["tags"]

	@classmethod
	def _update_field_config_data(cls, clazz, field, _type, modifiers, idx):
		if "tags" in field:
			tags = field["tags"]
		else:
			tags = list()

		if "_no_proxy" in tags:
			tags = list()
			tags.append("_no_proxy")
		else:
			type_kind = TypeKind.from_id(_type)
			if type_kind == TypeKind.JAVA_PUBLIC_STATIC_FIELD:
				tags.append("_static")
				if "type" in field:
					field_type = field["type"]
					if field_type["type"] == clazz["name"]:
						if "children" not in field_type:
							tags.append("_singleton")
			elif type_kind == TypeKind.JAVA_PUBLIC_INSTANCE_FIELD:
				tags.append("_instance")
			if "_no_proxy" in tags:
				tags.remove("_no_proxy")
			tags.append("_proxy")

		tags = sorted(list(set(tags)))
		if len(tags) > 0:
			field["tags"] = tags
		else:
			if "tags" in field:
				del field["tags"]

	@classmethod
	def _find_or_create_constructor_config_data(cls, constructors, constructor_name):
		the_constructor = dict()
		constructors.append(the_constructor)
		the_constructor["name"] = constructor_name
		the_constructor["params"] = the_constructor.get("params", list())
		return the_constructor

	@classmethod
	def _find_or_create_function_config_data(cls, functions, function_name):
		the_function = dict()
		functions.append(the_function)
		the_function["name"] = function_name
		the_function["params"] = the_function.get("params", list())
		the_function["returns"] = the_function.get("returns", list())
		return the_function

	@classmethod
	def _find_or_create_field_config_data(cls, fields, field_name):
		the_field = None
		for field in fields:
			if field["name"] == field_name:
				the_field = field
				break
		if not the_field:
			the_field = dict()
			fields.append(the_field)
		the_field["name"] = field_name
		return the_field

	@classmethod
	def _find_or_create_return_config_data(cls, returns, return_type_hierarchy):
		the_return_type_hierarchy = None
		for a_return_type_hierarchy in returns:
			if type_hierarchy_matches(a_return_type_hierarchy, return_type_hierarchy):
				the_return_type_hierarchy = a_return_type_hierarchy
				break
		if not the_return_type_hierarchy:
			the_return_type_hierarchy = return_type_hierarchy
			returns.append(the_return_type_hierarchy)
		return the_return_type_hierarchy

	@classmethod
	def _find_or_create_param_config_data(cls, params, param_type_hierarchy):
		the_param_type_hierarchy = param_type_hierarchy
		params.append(the_param_type_hierarchy)
		return the_param_type_hierarchy

	@classmethod
	def _find_or_create_field_type_config_data(cls, field, field_type_hierarchy):
		the_field_type_hierarchy = None
		if "type" in field:
			the_field_type_hierarchy = field["type"]
		if not the_field_type_hierarchy:
			the_field_type_hierarchy = field_type_hierarchy
			field["type"] = the_field_type_hierarchy
		return the_field_type_hierarchy

	@classmethod
	def _create_type_hierarchy(cls, type_id):
		type_hierarchy = TypeHierarchy_create(type_id)
		return type_hierarchy

	@classmethod
	def _build_type_hierarchy_structure(cls, type_hierarchy):
		structure = dict()
		class_name = type_hierarchy._class_name
		if class_name == 'com.zynga.sdk.cxx.CXXType$Array':
			class_name = '_object_array_type' # Special type marker representing Java array
			if type_hierarchy.child_count > 0:
				children = type_hierarchy.get_children()
				child = children[0]
				child_class_name = child._class_name
				type_kind = PrimitiveType.from_id(child_class_name)
				if type_kind is not None:
					class_name = '_%s_array_type' % child_class_name
		structure["type"] = class_name
		if type_hierarchy.child_count > 0:
			structure["children"] = list()
			children = type_hierarchy.get_children()
			for child in children:
				child_structure = TranslationUnit._build_type_hierarchy_structure(child)
				structure["children"].append(child_structure)
		return structure


class DummyType(Type):

	def __init__(self, kind_id):
		self._kind_id = kind_id

	@property
	def kind(self):
		return TypeKind.from_id(self._kind_id)

	@property
	def translation_unit(self):
		return None

class DummyCursor(Cursor):

	def __init__(self, parent_name, displayname, kind_id, type):
		self._parent_name = parent_name
		self._displayname = displayname
		self._kind_id = kind_id
		self._type = type

	def get_children(self):
		if not hasattr(self, '_children'):
			self._children = []
		return self._children

	@property
	def kind(self):
		return CursorKind.from_id(self._kind_id)

	@property
	def displayname(self):
		return self._displayname

	@property
	def description(self):
		return self._displayname

	@property
	def type(self):
		return self._type

	@property
	def enum_values(self):
		if not hasattr(self, '_enum_values'):
			self._enum_values = []
		return self._enum_values

	@property
	def parent_name(self):
		return self._parent_name

# Utility Functions

def type_hierarchy_matches(type_hierarchy_1, type_hierarchy_2):
	if type(type_hierarchy_1) is dict and type(type_hierarchy_2) is dict:
		type_hierarchy_1 = dict(type_hierarchy_1)
		type_hierarchy_keys = ['type','children']
		for key in type_hierarchy_1:
			if key not in type_hierarchy_keys:
				del type_hierarchy_1[key]
		type_hierarchy_2 = dict(type_hierarchy_2)
		for key in type_hierarchy_2:
			if key not in type_hierarchy_keys:
				del type_hierarchy_2[key]
		symm_set = set(type_hierarchy_1.keys()) ^ set(type_hierarchy_2.keys())
		if len(symm_set) > 0:
			return False
		for key in type_hierarchy_1:
			matches = type_hierarchy_matches(type_hierarchy_1[key], type_hierarchy_2[key])
			if not matches:
				return False
	elif type(type_hierarchy_1) is list and type(type_hierarchy_2) is list:
		if len(type_hierarchy_1) != len(type_hierarchy_2):
			return False
		for idx in range(0,len(type_hierarchy_1),1):
			matches = type_hierarchy_matches(type_hierarchy_1[idx], type_hierarchy_2[idx])
			if not matches:
				return False
	elif type(type_hierarchy_1) is str and type(type_hierarchy_2) is str:
		if type_hierarchy_1 != type_hierarchy_2:
			return False
	return True



# Index Functions
Index_create=lib.createIndex
Index_create.argtypes = [c_char_p]
Index_create.restype = c_object_p

Index_status=lib.indexStatus
Index_status.argtypes = []
Index_status.restype = c_int

Index_statusMessage=lib.indexStatusMessage
Index_statusMessage.argtypes = []
Index_statusMessage.restype = c_char_p

Index_destroy=lib.destroyIndex
Index_destroy.argtypes = []
Index_destroy.restype = c_int

# Translation Unit Functions

TranslationUnit_classes_visit_callback = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int, c_char_p, c_int, c_long, py_object)
TranslationUnit_classes_visit = lib.visitTranslationUnitClasses
TranslationUnit_classes_visit.argtypes = [(c_char * STR_ATTR_SIZE) * MAX_PACKAGE_COUNT, c_int, (c_char * STR_ATTR_SIZE) * MAX_CLASSE_COUNT, c_int, TranslationUnit_classes_visit_callback, py_object]

TranslationUnit_parse = lib.parseTranslationUnit
TranslationUnit_parse.argtypes = [Index, c_char_p]
TranslationUnit_parse.restype = c_object_p

TranslationUnit_dispose = lib.disposeTranslationUnit
TranslationUnit_dispose.argtypes = [TranslationUnit]

TranslationUnit_cursor = lib.getTranslationUnitCursor
TranslationUnit_cursor.argtypes = [TranslationUnit]
TranslationUnit_cursor.restype = Cursor
TranslationUnit_cursor.errcheck = Cursor.from_result

# Cursor Functions

Cursor_displayname = lib.getCursorDisplayName
Cursor_displayname.argtypes = [Cursor]
Cursor_displayname.restype = c_char_p

# TODO: Deprecated - Remove 
Cursor_description = lib.getCursorDescription
Cursor_description.argtypes = [Cursor]
Cursor_description.restype = c_char_p

Cursor_type = lib.getCursorType
Cursor_type.argtypes = [Cursor]
Cursor_type.restype = Type
Cursor_type.errcheck = Type.from_result

Cursor_visit_callback = CFUNCTYPE(c_int, Cursor, Cursor, py_object)
Cursor_visit = lib.visitCursorChildren
Cursor_visit.argtypes = [Cursor, Cursor_visit_callback, py_object]
Cursor_visit.restype = c_uint

Cursor_enum_values_callback = CFUNCTYPE(c_int, c_char_p, py_object)
Cursor_enum_values = lib.visitEnumValues
Cursor_enum_values.argtypes = [Cursor, Type, Cursor_enum_values_callback, py_object]
Cursor_enum_values.restype = c_uint

Cursor_visit_attrs_callback = CFUNCTYPE(c_int, c_int, c_char_p, py_object)
Cursor_visit_attrs = lib.visitCursorAttrs
Cursor_visit_attrs.argtypes = [Cursor, Cursor_visit_attrs_callback, py_object]

Cursor_parent_name = lib.getCursorParentName
Cursor_parent_name.argtypes = [Cursor]
Cursor_parent_name.restype = c_char_p

Cursor_translationUnit = lib.getCursorTranslationUnit
Cursor_translationUnit.argtypes = [Cursor]
Cursor_translationUnit.restype = c_object_p

# Type Hierarchy Functions

TypeHierarchy_create = lib.createTypeHierarchy
TypeHierarchy_create.argtypes = [c_longlong]
TypeHierarchy_create.restype = TypeHierarchy
TypeHierarchy_create.errcheck = TypeHierarchy.from_result

TypeHierarchy_visit_callback = CFUNCTYPE(c_int, TypeHierarchy, TypeHierarchy, py_object)
TypeHierarchy_visit = lib.visitTypeHierarchyChildren
TypeHierarchy_visit.argtypes = [TypeHierarchy, TypeHierarchy_visit_callback, py_object]
TypeHierarchy_visit.restype = c_uint

TypeHierarchy_canCastClass1ToClass2 = lib.canCastClass1ToClass2
TypeHierarchy_canCastClass1ToClass2.argtypes = [c_char * STR_ATTR_SIZE,c_char * STR_ATTR_SIZE]
TypeHierarchy_canCastClass1ToClass2.restype = c_bool

# Globals
INDEX_OK = 0
INDEX_ERR = -1

