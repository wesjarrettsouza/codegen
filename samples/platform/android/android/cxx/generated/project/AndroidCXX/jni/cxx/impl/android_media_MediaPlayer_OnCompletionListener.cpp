/*
 * Implementation (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


 		 








// Generated Code 

#include <android_media_MediaPlayer_OnCompletionListener.hpp>
#include <jni.h>
#include <CXXContext.hpp>
#include <JNIContext.hpp>
// TODO: integrate with custom converters
#include <CXXConverter.hpp>
#include <AndroidCXXConverter.hpp>
// TODO: FIXME: add include package
// FIXME: remove after testing

#define LOG_TAG "android_media_MediaPlayer_OnCompletionListener"
#define LOGV(...) __android_log_print(ANDROID_LOG_VERBOSE, LOG_TAG, __VA_ARGS__)

using namespace AndroidCXX;

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
android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener(const android_media_MediaPlayer_OnCompletionListener& cc)
{
	LOGV("android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener(const android_media_MediaPlayer_OnCompletionListener& cc) enter");

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

	LOGV("android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener(const android_media_MediaPlayer_OnCompletionListener& cc) exit");
}
android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener(void * proxy)
{
	LOGV("android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener(void * proxy) enter");

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

	LOGV("android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener(void * proxy) exit");
}
// TODO: remove
// 
// 
// android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener()
// {
// 	LOGV("android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener() enter");	

// 	const char *methodName = "<init>";
// 	const char *methodSignature = "()V";
// 	const char *className = "android/media/MediaPlayer$OnCompletionListener";

// 	LOGV("android_media_MediaPlayer_OnCompletionListener className %d methodName %s methodSignature %s", className, methodName, methodSignature);

// 	CXXContext *ctx = CXXContext::sharedInstance();
// 	JNIContext *jni = JNIContext::sharedInstance();

// 	jni->pushLocalFrame();

// 	long cxxAddress = (long) this;
// 	LOGV("android_media_MediaPlayer_OnCompletionListener cxx address %d", cxxAddress);
// 	jobject proxiedComponent = ctx->findProxyComponent(cxxAddress);
// 	LOGV("android_media_MediaPlayer_OnCompletionListener jni address %d", proxiedComponent);

// 	if (proxiedComponent == 0)
// 	{
// 		jclass clazz = jni->getClassRef(className);

// 		proxiedComponent = jni->createNewObject(clazz,jni->getMethodID(clazz, "<init>", methodSignature));
// 		proxiedComponent = jni->localToGlobalRef(proxiedComponent);

// 		ctx->registerProxyComponent(cxxAddress, proxiedComponent);
// 	}

// 	jni->popLocalFrame();

// 	LOGV("android_media_MediaPlayer_OnCompletionListener::android_media_MediaPlayer_OnCompletionListener() exit");	
// }
// 
// 
// Public Constructors
// Default Instance Destructor
android_media_MediaPlayer_OnCompletionListener::~android_media_MediaPlayer_OnCompletionListener()
{
	LOGV("android_media_MediaPlayer_OnCompletionListener::~android_media_MediaPlayer_OnCompletionListener() enter");
	CXXContext *ctx = CXXContext::sharedInstance();
	long address = (long) this;
	jobject proxiedComponent = ctx->findProxyComponent(address);
	if (proxiedComponent != 0)
	{
		JNIContext *jni = JNIContext::sharedInstance();
		ctx->deregisterProxyComponent(address);
	}		
	LOGV("android_media_MediaPlayer_OnCompletionListener::~android_media_MediaPlayer_OnCompletionListener() exit");
}
// Functions
void android_media_MediaPlayer_OnCompletionListener::onCompletion(AndroidCXX::android_media_MediaPlayer& arg0)
{
	LOGV("void android_media_MediaPlayer_OnCompletionListener::onCompletion(AndroidCXX::android_media_MediaPlayer& arg0) enter");

	const char *methodName = "onCompletion";
	const char *methodSignature = "(Landroid/media/MediaPlayer;)V";
	const char *className = "android/media/MediaPlayer$OnCompletionListener";

	LOGV("android_media_MediaPlayer_OnCompletionListener className %d methodName %s methodSignature %s", className, methodName, methodSignature);

	CXXContext *ctx = CXXContext::sharedInstance();
	JNIContext *jni = JNIContext::sharedInstance();

	jni->pushLocalFrame();

	long cxxAddress = (long) this;
	LOGV("android_media_MediaPlayer_OnCompletionListener cxx address %d", cxxAddress);
	jobject javaObject = ctx->findProxyComponent(cxxAddress);
	LOGV("android_media_MediaPlayer_OnCompletionListener jni address %d", javaObject);

	jobject jarg0;
	{
		long cxx_value = (long) & arg0;
		long java_value = 0;

		CXXTypeHierarchy cxx_type_hierarchy;
		std::stack<CXXTypeHierarchy> cxx_type_hierarchy_stack;
		
		cxx_type_hierarchy_stack.push(cxx_type_hierarchy);
		{
			CXXTypeHierarchy cxx_type_hierarchy = cxx_type_hierarchy_stack.top();
			cxx_type_hierarchy_stack.pop();
			cxx_type_hierarchy.type_name = std::string("android.media.MediaPlayer");
		}
		std::stack<long> converter_stack;
		converter_t converter_type = (converter_t) CONVERT_TO_JAVA;
		convert_android_media_MediaPlayer(java_value,cxx_value,cxx_type_hierarchy,converter_type,converter_stack);

		// Convert to JNI
		jarg0 = convert_jni_java_lang_Object_to_jni(java_value);
	}

	jni->invokeVoidMethod(javaObject,className,methodName,methodSignature,jarg0);
		
	jni->popLocalFrame();

	LOGV("void android_media_MediaPlayer_OnCompletionListener::onCompletion(AndroidCXX::android_media_MediaPlayer& arg0) exit");

}
