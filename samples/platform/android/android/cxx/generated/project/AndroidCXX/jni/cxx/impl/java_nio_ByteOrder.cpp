/*
 * Implementation (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



	
	









// Generated Code 

#include <java_nio_ByteOrder.hpp>
#include <jni.h>
#include <CXXContext.hpp>
#include <JNIContext.hpp>
// TODO: integrate with custom converters
#include <CXXConverter.hpp>
#include <AndroidCXXConverter.hpp>

#define LOG_TAG "java_nio_ByteOrder"
#define LOGV(...) __android_log_print(ANDROID_LOG_VERBOSE, LOG_TAG, __VA_ARGS__)

using namespace AndroidCXX;

static long static_obj;
static long static_address = (long) &static_obj;

// Default Instance Constructors
java_nio_ByteOrder::java_nio_ByteOrder(const java_nio_ByteOrder& cc)
{
	LOGV("java_nio_ByteOrder::java_nio_ByteOrder(const java_nio_ByteOrder& cc) enter");

	CXXContext *ctx = CXXContext::sharedInstance();
	long ccaddress = (long) &cc;
	LOGV("registerProxyComponent ccaddress %ld", ccaddress);
	jobject proxiedCCComponent = ctx->findProxyComponent(ccaddress);
	LOGV("registerProxyComponent proxiedCCComponent %ld", (long) proxiedCCComponent);
	long address = (long) this;
	LOGV("registerProxyComponent address %ld", address);
	jobject proxiedComponent = ctx->findProxyComponent(address);
	LOGV("registerProxyComponent proxiedComponent %d", proxiedComponent);
	if (proxiedComponent == 0)
	{
		JNIContext *jni = JNIContext::sharedInstance();
		proxiedComponent = proxiedCCComponent;
		LOGV("registerProxyComponent registering proxied component %ld using %d", proxiedComponent, address);
		ctx->registerProxyComponent(address, proxiedComponent);
	}

	LOGV("java_nio_ByteOrder::java_nio_ByteOrder(const java_nio_ByteOrder& cc) exit");
}
java_nio_ByteOrder::java_nio_ByteOrder(void * proxy)
{
	LOGV("java_nio_ByteOrder::java_nio_ByteOrder(void * proxy) enter");

	CXXContext *ctx = CXXContext::sharedInstance();
	long address = (long) this;
	LOGV("registerProxyComponent address %d", address);
	jobject proxiedComponent = ctx->findProxyComponent(address);
	LOGV("registerProxyComponent proxiedComponent %d", proxiedComponent);
	if (proxiedComponent == 0)
	{
		JNIContext *jni = JNIContext::sharedInstance();
		proxiedComponent = jni->localToGlobalRef((jobject) proxy);
		ctx->registerProxyComponent(address, proxiedComponent);
	}

	LOGV("java_nio_ByteOrder::java_nio_ByteOrder(void * proxy) exit");
}
java_nio_ByteOrder::java_nio_ByteOrder()
{
	LOGV("java_nio_ByteOrder::java_nio_ByteOrder() enter");	

	const char *methodName = "<init>";
	const char *methodSignature = "()V";
	const char *className = "java/nio/ByteOrder";

	LOGV("java_nio_ByteOrder className %d methodName %s methodSignature %s", className, methodName, methodSignature);

	CXXContext *ctx = CXXContext::sharedInstance();
	JNIContext *jni = JNIContext::sharedInstance();

	jni->pushLocalFrame();

	long cxxAddress = (long) this;
	LOGV("java_nio_ByteOrder cxx address %d", cxxAddress);
	jobject proxiedComponent = ctx->findProxyComponent(cxxAddress);
	LOGV("java_nio_ByteOrder jni address %d", proxiedComponent);

	if (proxiedComponent == 0)
	{
		jclass clazz = jni->getClassRef(className);

		proxiedComponent = jni->createNewObject(clazz,jni->getMethodID(clazz, "<init>", methodSignature));
		proxiedComponent = jni->localToGlobalRef(proxiedComponent);

		ctx->registerProxyComponent(cxxAddress, proxiedComponent);
	}

	jni->popLocalFrame();

	LOGV("java_nio_ByteOrder::java_nio_ByteOrder() exit");	
}
// Public Constructors
// Default Instance Destructor
java_nio_ByteOrder::~java_nio_ByteOrder()
{
	LOGV("java_nio_ByteOrder::~java_nio_ByteOrder() enter");
	CXXContext *ctx = CXXContext::sharedInstance();
	long address = (long) this;
	jobject proxiedComponent = ctx->findProxyComponent(address);
	if (proxiedComponent != 0)
	{
		JNIContext *jni = JNIContext::sharedInstance();
		ctx->deregisterProxyComponent(address);
	}		
	LOGV("java_nio_ByteOrder::~java_nio_ByteOrder() exit");
}
// Functions
java_lang_String java_nio_ByteOrder::toString()
{
	LOGV("java_lang_String java_nio_ByteOrder::toString() enter");

	const char *methodName = "toString";
	const char *methodSignature = "()Ljava/lang/String;";
	const char *className = "java/nio/ByteOrder";

	LOGV("java_nio_ByteOrder className %d methodName %s methodSignature %s", className, methodName, methodSignature);

	CXXContext *ctx = CXXContext::sharedInstance();
	JNIContext *jni = JNIContext::sharedInstance();

	jni->pushLocalFrame();

	long cxxAddress = (long) this;
	LOGV("java_nio_ByteOrder cxx address %d", cxxAddress);
	jobject javaObject = ctx->findProxyComponent(cxxAddress);
	LOGV("java_nio_ByteOrder jni address %d", javaObject);


	java_lang_String result;
	jstring jni_result = (jstring) jni->invokeObjectMethod(javaObject,className,methodName,methodSignature);
	long cxx_value = (long) 0;
	long java_value = convert_jni_string_to_java(jni_result);
	{
		CXXTypeHierarchy cxx_type_hierarchy;
		std::stack<CXXTypeHierarchy> cxx_type_hierarchy_stack;
		
		cxx_type_hierarchy_stack.push(cxx_type_hierarchy);
		{
			CXXTypeHierarchy cxx_type_hierarchy = cxx_type_hierarchy_stack.top();
			cxx_type_hierarchy_stack.pop();
			cxx_type_hierarchy.type_name = std::string("java.lang.String");
		}
		std::stack<long> converter_stack;
		converter_t converter_type = (converter_t) CONVERT_TO_CXX;
		convert_java_lang_String(java_value,cxx_value,cxx_type_hierarchy,converter_type,converter_stack);
	}
	result = (java_lang_String) (java_lang_String((java_lang_String *) cxx_value));
		
	jni->popLocalFrame();

	LOGV("java_lang_String java_nio_ByteOrder::toString() exit");

	return result;
}
java_nio_ByteOrder java_nio_ByteOrder::nativeOrder()
{
	LOGV("java_nio_ByteOrder java_nio_ByteOrder::nativeOrder() enter");

	const char *methodName = "nativeOrder";
	const char *methodSignature = "()Ljava/nio/ByteOrder;";
	const char *className = "java/nio/ByteOrder";

	LOGV("java_nio_ByteOrder className %d methodName %s methodSignature %s", className, methodName, methodSignature);

	CXXContext *ctx = CXXContext::sharedInstance();
	JNIContext *jni = JNIContext::sharedInstance();

	jni->pushLocalFrame();

	long cxxAddress = (long) static_address; // _static function
	LOGV("java_nio_ByteOrder cxx address %d", cxxAddress);
	jobject javaObject = ctx->findProxyComponent(cxxAddress);
	LOGV("java_nio_ByteOrder jni address %d", javaObject);


	java_nio_ByteOrder result;
	jobject jni_result = (jobject) jni->invokeObjectMethod(javaObject,className,methodName,methodSignature);
	long cxx_value = (long) 0;
	long java_value = convert_jni_java_lang_Object_to_java(jni_result);
	{
		CXXTypeHierarchy cxx_type_hierarchy;
		std::stack<CXXTypeHierarchy> cxx_type_hierarchy_stack;
		
		cxx_type_hierarchy_stack.push(cxx_type_hierarchy);
		{
			CXXTypeHierarchy cxx_type_hierarchy = cxx_type_hierarchy_stack.top();
			cxx_type_hierarchy_stack.pop();
			cxx_type_hierarchy.type_name = std::string("java.nio.ByteOrder");
		}
		std::stack<long> converter_stack;
		converter_t converter_type = (converter_t) CONVERT_TO_CXX;
		convert_java_nio_ByteOrder(java_value,cxx_value,cxx_type_hierarchy,converter_type,converter_stack);
	}
	result = (java_nio_ByteOrder) (java_nio_ByteOrder((java_nio_ByteOrder *) cxx_value));
		
	jni->popLocalFrame();

	LOGV("java_nio_ByteOrder java_nio_ByteOrder::nativeOrder() exit");

	return result;
}
