Description
============
This project provides a Python tool to generate C++ classes that proxy native abstract data types. Currently Android and iOS platforms are supported.

Setup
============
After cloning this repository, be sure to udpate and initialize all submodules with

	git submodule update --init --recursive

Using The Tool
============
Relative to the root of this repository the tool is located in `generator/generator.py`. Usage and options can be output by running `python generator/generator.py`.

Platform specific details are as follows:

iOS
------------
The following `generator.py` options currently have no effect: `--file`, `--wrapper-file`, `--generate-reports`, `--generate-projects`, `--generate-wrapper-code`, `--generate-wrapper-projects`, `--include-wrapper-package`, `--include-wrapper-package-rel-path`.

------------

`--generate-config`: Uses the input config file specified with `--config`. The input config file must contain a Python dictionary named `config` that contains at least two keys, `"frameworks"` and `"interfaces"`, both of which map to lists of strings. An additional key `"clang_opts"`, mapping to a dictionary, can be specified.

The frameworks list currently only supports a single framework (an arbitrary number of frameworks may be supported in the future) referenced by absolute path.

The interfaces list may contain zero or more names of Objective-C interfaces; if no interfaces are specified the tool infers all interfaces.

If the clang_opts dictionary is specified, the string mapped to by key, `"metadata"`, will be passed as options to the clang compiler. While default clang options are inferred, you'll likely need to specify your own to avoid any errors while generating the config.

The `--generate-config` option signifies that the tool should iterate over each of the methods of the specified interfaces for the given framework and emit a config file containing every parameter and return value's type and conversion data. The tool will additionally emit method data for all interfaces and protocols in the framework that are used as a parameter or return value. In other words, the tool emits method data for the dependency closure of the specified interfaces and framework. The `--output-dir` option specifies where the emitted config will be located.

-------------

`--generate-code`: Uses the input config file specified with `--config`; emits code for config objects that contain the `"_proxy"` tag and objects with the `"_no_proxy"` tag will not emit code. Generates proxy classes for all interfaces and protocols specified in the config, enums for each specified enum, and abstract classes for each specified protocol.

For output directory `(OUTPUT)` and package `(PACKAGE)`, given by the `--output-dir` and `--package` options, all header files will be located in `(OUTPUT)/project/includes/(PACKAGE)` and all implementation files will be located in `(OUTPUT)/project/impl/(PACKAGE)`.

A makefile is generated in the `(OUTPUT)/project` folder. The makefile will compile and archive all source files for a set of architectures determined by the config's clang_opts dictionary. The clang_opts dictionary must contain a `"makefile"` key which maps to a dictionay. Each key in the makefile dictionay represents an architecture to build and the mapped string will be passed as options to the clang compiler. Default makefile values are generated by the `--generate-config` option.



Samples
============

iOS
------------
The `samples/platforms/ios/facebook` directory contains an example of how to use this tool to generate proxies for nearly all of `FacebookSDK.framework`. The latest FacebookSDK framework is located in the `objc` subdirectory. An example of using the generated Facebook API to perform basic tasks is located under the `TestFacebookCXX` subdirectory. Two shell scripts wrap the `--generate-config` and `--generate-code` invocations of this tool under the `cxx` subdirectory. The input config file and generated code are also located under the `cxx` subdirectory.

First, run the `generate_config.sh` script from the `cxx` directory via 

	./generate_config.sh

It may take half a minute to create the AST of the `FacebookSDK.framework` headers and parse the metadata.


------------

_Note_

Under the current FacebookSDK version, the file `FBErrorUtility.h` doesn't import the Foundation objects. This results in compilation errors and prevents us from creating a proxy for the FBErrorUtility interface. Once the tool is done generating the config, open it and perform a search for `FBErrorUtility`, then set the `"_proxy"` tag to `"_no_proxy"`.

------------

There are also several functions which are set to `"_no_proxy"` because no appropriate converter was found for them. You can find these by performing a search for `"_TODO_"`.

Once the config file is generated, run the `generate_code.sh` script from the `cxx` directory via 

	./generate_code.sh

This should only take a few seconds.

To build a static library for the `armv7` and `i386` architectures, change to the `generated/project` subdirectory and run `make`. The fat library will be located under the `lib/fat` subdirectory after completion.

Open the `TestFacebookCXX` Xcode project and notice that the target's `Header Search Path` settings contains the generated includes directory. Also notice that the project links with the fat library that we created with make. This project uses Objective-C for the UI, but all button callbacks are written in C++. If you have the appropriate provisioning and signing profile you can build and run this project.


Repository Organization
============
Relative to the root of the repository, here are some key file locations:

- A common generator python script is located in `generator/generator.py`
- Platform dependent generator source code is located under `generator/platforms/(PLATFORM)/generator/(PLATFORM)generator.py`
- Samples and example code for each platform are located under `samples/platforms/(PLATFORM)`

iOS
------------
- A clang tool submodule is located under `generator/platforms/ios/generator/indexer/clocxml`. This tool emits an XML representation of Objective-C abstract data types.
- A Python script which parses the XML emitted by the clocxml tool is located in `generator/platforms/ios/generator/indexer/ocindex.py`.
- The default converter configuration files are located in `generator/platforms/ios/generator/converters/occonverter.py`
- Cheetah Template files for emitting C++ code are located in `generator/platforms/ios/generator/templates`

