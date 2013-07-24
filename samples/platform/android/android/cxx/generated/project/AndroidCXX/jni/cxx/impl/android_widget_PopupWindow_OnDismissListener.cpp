/*
 * Implementation (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//










// Generated Code 

#include <android_widget_PopupWindow_OnDismissListener.hpp>
#include <jni.h>
#include <CXXContext.hpp>
#include <JNIContext.hpp>
// TODO: integrate with custom converters
#include <CXXConverter.hpp>
#include <AndroidCXXConverter.hpp>
// TODO: FIXME: add include package
// FIXME: remove after testing

#define LOG_TAG "android_widget_PopupWindow_OnDismissListener"
#define LOGV(...) __android_log_print(ANDROID_LOG_VERBOSE, LOG_TAG, __VA_ARGS__)

using namespace AndroidCXX;

// 
// 

static long static_obj;
static long static_address = (long) &static_obj;

// Default Instance Constructors
android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener(const android_widget_PopupWindow_OnDismissListener& cc)
{
	LOGV("android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener(const android_widget_PopupWindow_OnDismissListener& cc) enter");

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

	LOGV("android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener(const android_widget_PopupWindow_OnDismissListener& cc) exit");
}
android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener(void * proxy)
{
	LOGV("android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener(void * proxy) enter");

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

	LOGV("android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener(void * proxy) exit");
}
// TODO: remove
// 
// 
// android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener()
// {
// 	LOGV("android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener() enter");	

// 	const char *methodName = "<init>";
// 	const char *methodSignature = "()V";
// 	const char *className = "android/widget/PopupWindow$OnDismissListener";

// 	LOGV("android_widget_PopupWindow_OnDismissListener className %d methodName %s methodSignature %s", className, methodName, methodSignature);

// 	CXXContext *ctx = CXXContext::sharedInstance();
// 	JNIContext *jni = JNIContext::sharedInstance();

// 	jni->pushLocalFrame();

// 	long cxxAddress = (long) this;
// 	LOGV("android_widget_PopupWindow_OnDismissListener cxx address %d", cxxAddress);
// 	jobject proxiedComponent = ctx->findProxyComponent(cxxAddress);
// 	LOGV("android_widget_PopupWindow_OnDismissListener jni address %d", proxiedComponent);

// 	if (proxiedComponent == 0)
// 	{
// 		jclass clazz = jni->getClassRef(className);

// 		proxiedComponent = jni->createNewObject(clazz,jni->getMethodID(clazz, "<init>", methodSignature));
// 		proxiedComponent = jni->localToGlobalRef(proxiedComponent);

// 		ctx->registerProxyComponent(cxxAddress, proxiedComponent);
// 	}

// 	jni->popLocalFrame();

// 	LOGV("android_widget_PopupWindow_OnDismissListener::android_widget_PopupWindow_OnDismissListener() exit");	
// }
// 
// 
// Public Constructors
// Default Instance Destructor
android_widget_PopupWindow_OnDismissListener::~android_widget_PopupWindow_OnDismissListener()
{
	LOGV("android_widget_PopupWindow_OnDismissListener::~android_widget_PopupWindow_OnDismissListener() enter");
	CXXContext *ctx = CXXContext::sharedInstance();
	long address = (long) this;
	jobject proxiedComponent = ctx->findProxyComponent(address);
	if (proxiedComponent != 0)
	{
		JNIContext *jni = JNIContext::sharedInstance();
		ctx->deregisterProxyComponent(address);
	}		
	LOGV("android_widget_PopupWindow_OnDismissListener::~android_widget_PopupWindow_OnDismissListener() exit");
}
// Functions
void android_widget_PopupWindow_OnDismissListener::onDismiss()
{
	LOGV("void android_widget_PopupWindow_OnDismissListener::onDismiss() enter");

	const char *methodName = "onDismiss";
	const char *methodSignature = "()V";
	const char *className = "android/widget/PopupWindow$OnDismissListener";

	LOGV("android_widget_PopupWindow_OnDismissListener className %d methodName %s methodSignature %s", className, methodName, methodSignature);

	CXXContext *ctx = CXXContext::sharedInstance();
	JNIContext *jni = JNIContext::sharedInstance();

	jni->pushLocalFrame();

	long cxxAddress = (long) this;
	LOGV("android_widget_PopupWindow_OnDismissListener cxx address %d", cxxAddress);
	jobject javaObject = ctx->findProxyComponent(cxxAddress);
	LOGV("android_widget_PopupWindow_OnDismissListener jni address %d", javaObject);


	jni->invokeVoidMethod(javaObject,className,methodName,methodSignature);
		
	jni->popLocalFrame();

	LOGV("void android_widget_PopupWindow_OnDismissListener::onDismiss() exit");

}
