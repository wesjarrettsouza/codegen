/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


 		 
 		 
 		 
 		 








// Generated Code 

#ifndef _android_app_PendingIntent_OnFinished
#define _android_app_PendingIntent_OnFinished
//
// Scroll Down 
//


#include <android_app_PendingIntent.hpp>

#include <android_content_Intent.hpp>

#include <java_lang_String.hpp>

#include <android_os_Bundle.hpp>

#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>
#include <CXXTypes.hpp>


#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace AndroidCXX {

// Forward Declarations

class android_app_PendingIntent;

class android_content_Intent;

class java_lang_String;

class android_os_Bundle;

class android_app_PendingIntent_OnFinished
{
public:

	android_app_PendingIntent_OnFinished(const android_app_PendingIntent_OnFinished& cc);
	android_app_PendingIntent_OnFinished(void * proxy);
	// Public Constructors
	// TODO: remove
	// 
	// android_app_PendingIntent_OnFinished();
	// 
	// Default Destructor
	virtual ~android_app_PendingIntent_OnFinished();
	// Functions
	 void onSendFinished(AndroidCXX::android_app_PendingIntent& arg0,AndroidCXX::android_content_Intent& arg1,int& arg2,AndroidCXX::java_lang_String& arg3,AndroidCXX::android_os_Bundle& arg4);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_app_PendingIntent_OnFinished