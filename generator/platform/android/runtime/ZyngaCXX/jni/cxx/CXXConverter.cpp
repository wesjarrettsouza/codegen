/*
 * CXXConverter.cpp
 * ZyngaCXX
 *
 * Created on: June 29, 2013
 * Author: rvergis
 *
 * Copyright (c) 2013 Zynga. All rights reserved.
 */

#include <CXXConverter.hpp>
#include <CXXTypeHierarchy.hpp>
#include <CXXContext.hpp>
#include <JNIContext.hpp>
#include <jni.h>
#include <cstdarg>
#include <string>
#include <vector>
#include <stack>
#include <map>

#define LOG_TAG "JDKCXXConverter"
#define LOGV(...) __android_log_print(ANDROID_LOG_VERBOSE, LOG_TAG, __VA_ARGS__)

cxx_converter get_converter(std::stack<long>& converter_stack)
{
	long converter_ptr = converter_stack.top();
	converter_stack.pop();
	cxx_converter converter = (cxx_converter) converter_ptr;
	return converter;
}

void convert_boolean(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	if (converter_type == CONVERT_TO_JAVA)
	{
		java_value = cxx_value;
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		cxx_value = java_value;
	}
}

void convert_byte(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	if (converter_type == CONVERT_TO_JAVA)
	{
		java_value = cxx_value;
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		cxx_value = java_value;
	}
}

void convert_char(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	if (converter_type == CONVERT_TO_JAVA)
	{
		java_value = cxx_value;
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		cxx_value = java_value;
	}
}

void convert_short(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	if (converter_type == CONVERT_TO_JAVA)
	{
		java_value = cxx_value;
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		cxx_value = java_value;
	}
}

void convert_int(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	if (converter_type == CONVERT_TO_JAVA)
	{
		java_value = cxx_value;
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		cxx_value = java_value;
	}
}

void convert_long(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	if (converter_type == CONVERT_TO_JAVA)
	{
		java_value = cxx_value;
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		cxx_value = java_value;
	}
}

void convert_float(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	if (converter_type == CONVERT_TO_JAVA)
	{
		java_value = cxx_value;
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		cxx_value = java_value;
	}
}

void convert_double(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	if (converter_type == CONVERT_TO_JAVA)
	{
		java_value = cxx_value;
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		cxx_value = java_value;
	}
}

void convert__object_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();

		cxx_converter item_converter = get_converter(converter_stack);

		std::vector<long> *cxx_vector = (std::vector<long> *) cxx_value;
		int count = cxx_vector->size();

		std::string child_type = jni->getJNIName( std::string("java.lang.Object") );
		CXXTypeHierarchy item_type;
		item_type.type_name = child_type;
		std::vector<CXXTypeHierarchy> child_types = cxx_type_hierarchy.child_types;
		if (child_types.size() > 0)
		{
			item_type = child_types.at(0);
			child_type = jni->getJNIName( item_type.type_name );
		}

		java_value = (long) jni->createObjectArray(count, jni->getClassRef( child_type.c_str() ));

		for(std::vector<long>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			long cxx_item_ptr = (long) *it;
			long java_item_ptr = 0;
			int item_idx = it - cxx_vector->begin();
			item_converter(java_item_ptr, cxx_item_ptr, item_type, converter_type, converter_stack);
			jni->setObjectArrayElement((jobjectArray) java_value, item_idx, (jobject) java_item_ptr);
		}

		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();

		std::string child_type = jni->getJNIName( std::string("java.lang.Object") );
		CXXTypeHierarchy item_type;
		item_type.type_name = child_type;
		std::vector<CXXTypeHierarchy> child_types = cxx_type_hierarchy.child_types;
		if (child_types.size() > 0)
		{
			item_type = child_types.at(0);
			child_type = jni->getJNIName( item_type.type_name );
		}

		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<long> *cxx_vector = (std::vector<long> *) cxx_value;
		int size = (int) jni->getArrayLength((jobjectArray) java_value);
		for (int idx = 0 ; idx < size; idx++)
		{
			long java_item_ptr = (long) jni->getObjectArrayElement((jobjectArray) java_value, idx);
			long cxx_item_ptr = 0;
			item_converter(java_item_ptr, cxx_item_ptr, item_type, converter_type, converter_stack);
			cxx_vector->push_back(cxx_item_ptr);
		}

		jni->popLocalFrame();
	}
}

void convert__byte_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<byte> *cxx_vector = (std::vector<byte> *) cxx_value;
		int count = cxx_vector->size();
		char java_array[count];
		int item_idx = 0;
		for(std::vector<byte>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			byte item = (byte) *it;
			java_array[item_idx++] = item;
		}
		java_value = (long) jni->createByteArray(*java_array, count);
		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<byte> *cxx_vector = new std::vector<byte>();
		int count = (int) jni->getArrayLength((jarray) java_value);
		char * java_array = jni->getByteArray((jbyteArray) java_value);
		for (int idx = 0 ; idx < count; idx++)
		{
			char item = (char) java_array[idx];
			cxx_vector->push_back((byte) item);
		}
		cxx_value = (long) cxx_vector;
		jni->popLocalFrame();
	}

	log("convert__byte_array_type exit");
}

void convert__char_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<char> *cxx_vector = (std::vector<char> *) cxx_value;
		int count = cxx_vector->size();
		char java_array[count];
		int item_idx = 0;
		for(std::vector<char>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			char item = (char) *it;
			java_array[item_idx++] = item;
		}
		java_value = (long) jni->createCharArray(*java_array, count);
		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<char> *cxx_vector = new std::vector<char>();
		int count = (int) jni->getArrayLength((jarray) java_value);
		char * java_array = jni->getCharArray((jcharArray) java_value);
		for (int idx = 0 ; idx < count; idx++)
		{
			char item = (char) java_array[idx];
			cxx_vector->push_back(item);
		}
		cxx_value = (long) cxx_vector;
		jni->popLocalFrame();
	}
}

void convert__short_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<short> *cxx_vector = (std::vector<short> *) cxx_value;
		int count = cxx_vector->size();
		short java_array[count];
		int item_idx = 0;
		for(std::vector<short>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			short item = (short) *it;
			java_array[item_idx++] = item;
		}
		java_value = (long) jni->createShortArray(*java_array, count);
		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<short> *cxx_vector = new std::vector<short>();
		int count = (int) jni->getArrayLength((jarray) java_value);
		short * java_array = jni->getShortArray((jshortArray) java_value);
		for (int idx = 0 ; idx < count; idx++)
		{
			short item = (short) java_array[idx];
			cxx_vector->push_back(item);
		}
		cxx_value = (long) cxx_vector;
		jni->popLocalFrame();
	}
}

void convert__int_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<int> *cxx_vector = (std::vector<int> *) cxx_value;
		int count = cxx_vector->size();
		int java_array[count];
		int item_idx = 0;
		for(std::vector<int>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			int item = (int) *it;
			java_array[item_idx++] = item;
		}
		java_value = (long) jni->createIntArray(*java_array, count);
		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<int> *cxx_vector = new std::vector<int>();
		int count = (int) jni->getArrayLength((jarray) java_value);
		int * java_array = jni->getIntArray((jintArray) java_value);
		for (int idx = 0 ; idx < count; idx++)
		{
			int item = (int) java_array[idx];
			cxx_vector->push_back(item);
		}
		cxx_value = (long) cxx_vector;
		jni->popLocalFrame();
	}
}

void convert__long_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<long> *cxx_vector = (std::vector<long> *) cxx_value;
		int count = cxx_vector->size();
		long java_array[count];
		int item_idx = 0;
		for(std::vector<long>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			long item = (long) *it;
			java_array[item_idx++] = item;
		}
		java_value = (long) jni->createLongArray(*java_array, count);
		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<long> *cxx_vector = new std::vector<long>();
		int count = (int) jni->getArrayLength((jarray) java_value);
		long * java_array = jni->getLongArray((jlongArray) java_value);
		for (int idx = 0 ; idx < count; idx++)
		{
			long item = (long) java_array[idx];
			cxx_vector->push_back(item);
		}
		cxx_value = (long) cxx_vector;
		jni->popLocalFrame();
	}
}

void convert__float_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<float> *cxx_vector = (std::vector<float> *) cxx_value;
		int count = cxx_vector->size();
		float java_array[count];
		int item_idx = 0;
		for(std::vector<float>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			float item = (float) *it;
			java_array[item_idx++] = item;
		}
		java_value = (long) jni->createFloatArray(*java_array, count);
		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<float> *cxx_vector = new std::vector<float>();
		int count = (int) jni->getArrayLength((jarray) java_value);
		float * java_array = jni->getFloatArray((jfloatArray) java_value);
		for (int idx = 0 ; idx < count; idx++)
		{
			float item = (float) java_array[idx];
			cxx_vector->push_back(item);
		}
		cxx_value = (long) cxx_vector;
		jni->popLocalFrame();
	}
}

void convert__double_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<double> *cxx_vector = (std::vector<double> *) cxx_value;
		int count = cxx_vector->size();
		double java_array[count];
		int item_idx = 0;
		for(std::vector<double>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			double item = (double) *it;
			java_array[item_idx++] = item;
		}
		java_value = (long) jni->createDoubleArray(*java_array, count);
		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<double> *cxx_vector = new std::vector<double>();
		int count = (int) jni->getArrayLength((jarray) java_value);
		double * java_array = jni->getDoubleArray((jdoubleArray) java_value);
		for (int idx = 0 ; idx < count; idx++)
		{
			double item = (double) java_array[idx];
			cxx_vector->push_back(item);
		}
		cxx_value = (long) cxx_vector;
		jni->popLocalFrame();
	}
}

void convert__boolean_array_type(long& java_value, long& cxx_value, const CXXTypeHierarchy cxx_type_hierarchy, const converter_t& converter_type, std::stack<long>& converter_stack)
{
	JNIContext *jni = JNIContext::sharedInstance();

	if (converter_type == CONVERT_TO_JAVA)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<bool> *cxx_vector = (std::vector<bool> *) cxx_value;
		int count = cxx_vector->size();
		bool java_array[count];
		int item_idx = 0;
		for(std::vector<bool>::iterator it = cxx_vector->begin(); it != cxx_vector->end(); ++it)
		{
			bool item = (bool) *it;
			java_array[item_idx++] = item;
		}
		java_value = (long) jni->createBooleanArray(*java_array, count);
		java_value = (long) jni->popLocalFrame((jobject) java_value);
	}
	else if (converter_type == CONVERT_TO_CXX)
	{
		jni->pushLocalFrame();
		cxx_converter item_converter = get_converter(converter_stack);
		std::vector<bool> *cxx_vector = new std::vector<bool>();
		int count = (int) jni->getArrayLength((jarray) java_value);
		bool * java_array = jni->getBooleanArray((jbooleanArray) java_value);
		for (int idx = 0 ; idx < count; idx++)
		{
			bool item = (bool) java_array[idx];
			cxx_vector->push_back(item);
		}
		cxx_value = (long) cxx_vector;
		jni->popLocalFrame();
	}
}

