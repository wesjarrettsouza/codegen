APP_PLATFORM=android-8
APP_ABI := armeabi
APP_STL := gnustl_static
NDK_MODULE_PATH := /Users/rvergis/Documents/cxx-bindings-generator/samples/platform/android/android/cxx/../../../../../generator/platform/android/generator/..:/Users/rvergis/Documents/cxx-bindings-generator/samples/platform/android/android/cxx/generated
#NDKR8 bug? the list of modules has to be explicitly listed to compile static
APP_MODULES := AndroidCXX_static
APP_CPPFLAGS := -fpermissive
