/*
 * Implementation (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


	








// Generated Code 

#include <com_facebook_widget_GraphObjectPagingLoader_PagedResults.hpp>
#include <jni.h>
#include <CXXContext.hpp>
#include <JNIContext.hpp>
// TODO: integrate with custom converters
#include <CXXConverter.hpp>
#include <FacebookCXXConverter.hpp>
// TODO: FIXME: add include package
// FIXME: remove after testing
#include <AndroidCXXConverter.hpp>

#define LOG_TAG "com_facebook_widget_GraphObjectPagingLoader_PagedResults"
#define LOGV(...) __android_log_print(ANDROID_LOG_VERBOSE, LOG_TAG, __VA_ARGS__)

using namespace FacebookCXX;

// 
// 
// 
// 
// 
// 
// 
// 

static long static_obj;
static long static_address = (long) &static_obj;

// Default Instance Constructors
com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults(const com_facebook_widget_GraphObjectPagingLoader_PagedResults& cc)
{
	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults(const com_facebook_widget_GraphObjectPagingLoader_PagedResults& cc) enter");

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

	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults(const com_facebook_widget_GraphObjectPagingLoader_PagedResults& cc) exit");
}
com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults(void * proxy)
{
	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults(void * proxy) enter");

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

	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults(void * proxy) exit");
}
// TODO: remove
// 
// 
// com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults()
// {
// 	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults() enter");	

// 	const char *methodName = "<init>";
// 	const char *methodSignature = "()V";
// 	const char *className = "com/facebook/widget/GraphObjectPagingLoader$PagedResults";

// 	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults className %d methodName %s methodSignature %s", className, methodName, methodSignature);

// 	CXXContext *ctx = CXXContext::sharedInstance();
// 	JNIContext *jni = JNIContext::sharedInstance();

// 	jni->pushLocalFrame();

// 	long cxxAddress = (long) this;
// 	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults cxx address %d", cxxAddress);
// 	jobject proxiedComponent = ctx->findProxyComponent(cxxAddress);
// 	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults jni address %d", proxiedComponent);

// 	if (proxiedComponent == 0)
// 	{
// 		jclass clazz = jni->getClassRef(className);

// 		proxiedComponent = jni->createNewObject(clazz,jni->getMethodID(clazz, "<init>", methodSignature));
// 		proxiedComponent = jni->localToGlobalRef(proxiedComponent);

// 		ctx->registerProxyComponent(cxxAddress, proxiedComponent);
// 	}

// 	jni->popLocalFrame();

// 	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults::com_facebook_widget_GraphObjectPagingLoader_PagedResults() exit");	
// }
// 
// 
// Public Constructors
// Default Instance Destructor
com_facebook_widget_GraphObjectPagingLoader_PagedResults::~com_facebook_widget_GraphObjectPagingLoader_PagedResults()
{
	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults::~com_facebook_widget_GraphObjectPagingLoader_PagedResults() enter");
	CXXContext *ctx = CXXContext::sharedInstance();
	long address = (long) this;
	jobject proxiedComponent = ctx->findProxyComponent(address);
	if (proxiedComponent != 0)
	{
		JNIContext *jni = JNIContext::sharedInstance();
		ctx->deregisterProxyComponent(address);
	}		
	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults::~com_facebook_widget_GraphObjectPagingLoader_PagedResults() exit");
}
// Functions
FacebookCXX::com_facebook_model_GraphObjectList com_facebook_widget_GraphObjectPagingLoader_PagedResults::getData()
{
	LOGV("FacebookCXX::com_facebook_model_GraphObjectList com_facebook_widget_GraphObjectPagingLoader_PagedResults::getData() enter");

	const char *methodName = "getData";
	const char *methodSignature = "()Lcom/facebook/model/GraphObjectList;";
	const char *className = "com/facebook/widget/GraphObjectPagingLoader$PagedResults";

	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults className %d methodName %s methodSignature %s", className, methodName, methodSignature);

	CXXContext *ctx = CXXContext::sharedInstance();
	JNIContext *jni = JNIContext::sharedInstance();

	jni->pushLocalFrame();

	long cxxAddress = (long) this;
	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults cxx address %d", cxxAddress);
	jobject javaObject = ctx->findProxyComponent(cxxAddress);
	LOGV("com_facebook_widget_GraphObjectPagingLoader_PagedResults jni address %d", javaObject);


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
			cxx_type_hierarchy.type_name = std::string("com.facebook.model.GraphObjectList");
			{
				CXXTypeHierarchy child_cxx_type_hierarchy;
				cxx_type_hierarchy.child_types.push_back(child_cxx_type_hierarchy);
				cxx_type_hierarchy_stack.push(child_cxx_type_hierarchy);
				
			}
		}
		{
			CXXTypeHierarchy cxx_type_hierarchy = cxx_type_hierarchy_stack.top();
			cxx_type_hierarchy_stack.pop();
			cxx_type_hierarchy.type_name = std::string("com.facebook.model.GraphObject");
		}
		std::stack<long> converter_stack;
		
		{
			{
				converter_stack.push((long) &convert_com_facebook_model_GraphObject);				

			}
		}
		converter_t converter_type = (converter_t) CONVERT_TO_CXX;
		convert_com_facebook_model_GraphObjectList(java_value,cxx_value,cxx_type_hierarchy,converter_type,converter_stack);
	}

	FacebookCXX::com_facebook_model_GraphObjectList result((FacebookCXX::com_facebook_model_GraphObjectList) *((FacebookCXX::com_facebook_model_GraphObjectList *) cxx_value));
	delete ((FacebookCXX::com_facebook_model_GraphObjectList *) cxx_value);
		
	jni->popLocalFrame();

	LOGV("FacebookCXX::com_facebook_model_GraphObjectList com_facebook_widget_GraphObjectPagingLoader_PagedResults::getData() exit");

	return result;
}
