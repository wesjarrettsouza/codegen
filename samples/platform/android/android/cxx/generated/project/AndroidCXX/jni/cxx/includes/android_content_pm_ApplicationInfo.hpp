/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


	
 		 
 		 
 		 
 		 
	


 		 












// Generated Code 

#ifndef _android_content_pm_ApplicationInfo
#define _android_content_pm_ApplicationInfo
//
// Scroll Down 
//


#include <java_lang_String.hpp>

#include <android_util_Printer.hpp>

#include <android_os_Parcel.hpp>

#include <android_content_pm_PackageManager.hpp>

#include <java_lang_CharSequence.hpp>


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

class java_lang_String;

class android_util_Printer;

class android_os_Parcel;

class android_content_pm_PackageManager;

class java_lang_CharSequence;

class android_content_pm_ApplicationInfo;

class android_content_pm_ApplicationInfo
{
public:

	android_content_pm_ApplicationInfo(const android_content_pm_ApplicationInfo& cc);
	android_content_pm_ApplicationInfo(void * proxy);
	// Public Constructors
	android_content_pm_ApplicationInfo();
	android_content_pm_ApplicationInfo(AndroidCXX::android_content_pm_ApplicationInfo& arg0);
	// TODO: remove
	// 
	// Default Destructor
	virtual ~android_content_pm_ApplicationInfo();
	// Functions
	 AndroidCXX::java_lang_String toString();
	 void dump(AndroidCXX::android_util_Printer& arg0,AndroidCXX::java_lang_String& arg1);
	 int describeContents();
	 void writeToParcel(AndroidCXX::android_os_Parcel& arg0,int& arg1);
	 AndroidCXX::java_lang_CharSequence loadDescription(AndroidCXX::android_content_pm_PackageManager& arg0);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_content_pm_ApplicationInfo