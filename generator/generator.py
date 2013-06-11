#!/usr/bin/env python
# generator.py
# c++ generator
#
# Copyright (c) 2011 - Zynga Inc.


# Base Generator class
# New platforms need to extend this class and implement the functions indicated

import exceptions
import sys
import os
import logging

class BaseGenerator(object):

	def __init__(self):
		self.config = None
		self.output_dir = None
	
	def setup(self):
		raise NotImplementedError("subclasses should implement setup()")

	def generate(self):
		raise NotImplementedError("subclasses should implement generate()")

	def generate_wrapper(self):
		raise NotImplementedError("subclasses should implement generate_wrapper()")

	def teardown(self):
		raise NotImplementedError("subclasses should implement teardown()")

def list_supported_platforms():
	return [name for name in os.listdir("platform") if os.path.isdir(os.path.join("platform", name))]

def create_platform_generator(platform_name):
	import imp
	generator_module_name = platform_name + "generator"
	sys.path.append(os.path.join("platform", platform_name, "generator"))
	filepath, pathname, description = imp.find_module(generator_module_name)
	platform_module = imp.load_module(generator_module_name, filepath, pathname, description)
	platform_class = getattr(platform_module, "Generator")
	platform_generator = platform_class()
	return platform_generator

def main():
	import optparse
	from optparse import OptionParser

	supported_platforms = list_supported_platforms()

	parser = OptionParser("usage: %prog [options] {configfile}")
	parser.add_option("--platform", action="store", type="string", dest="platform",
							help="Indicates the platform for which code will be generated. Supported platforms are " + str(supported_platforms))
	parser.add_option("--config", action="store", type="string", dest="config",
							help="Specifies the configuration file to be used for code generation")
	parser.add_option("--output-dir", action="store", type="string", dest="output_dir",
							help="Specifies the output directory where the code will be generated")
	parser.add_option("--generate-wrapper", action="store_true", dest="generate_wrapper", default=True,
							help="Flag to indicate if the wrapper file needs to be generated (default is True)")
	parser.add_option("--log",  action="store", type="string", dest="loglevel",
							help="Specifies the generator log level. Valid values are info (for INFO level logging) and debug (for DEBUG level logging)")
	(opts, args) = parser.parse_args()

	loglevel = "INFO"
	if opts.loglevel:
		loglevel = str(opts.loglevel).upper()
	logging.basicConfig(level=getattr(logging, loglevel))

	if not opts.platform:
		parser.print_help()
		sys.exit(1)

	if not opts.platform in supported_platforms:
		parser.print_help()
		sys.exit(1)

	if not opts.config:
		parser.print_help()
		sys.exit(1)	

	if not opts.output_dir:
		parser.print_help()
		sys.exit(1)

	platform_generator = create_platform_generator(opts.platform)
	platform_generator.config = opts.config
	platform_generator.output_dir = opts.output_dir

	platform_generator.setup()
	platform_generator.generate()
	if opts.generate_wrapper:
		platform_generator.generate_wrapper()
	platform_generator.teardown()

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print e
		sys.exit(1)