/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


	
 		 
 		 
	


 		 











// Generated Code 

#ifndef _android_content_pm_PermissionInfo
#define _android_content_pm_PermissionInfo
//
// Scroll Down 
//


#include <java_lang_String.hpp>

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

class android_os_Parcel;

class android_content_pm_PackageManager;

class java_lang_CharSequence;

class android_content_pm_PermissionInfo;

class android_content_pm_PermissionInfo
{
public:

	android_content_pm_PermissionInfo(Proxy proxy);
	// Public Constructors
	android_content_pm_PermissionInfo();
	android_content_pm_PermissionInfo(AndroidCXX::android_content_pm_PermissionInfo const& arg0);
	Proxy proxy() const;	
	// Default Destructor
	virtual ~android_content_pm_PermissionInfo();
	// Functions
	 AndroidCXX::java_lang_String toString();
	 int describeContents();
	 void writeToParcel(AndroidCXX::android_os_Parcel const& arg0,int const& arg1);
	 AndroidCXX::java_lang_CharSequence loadDescription(AndroidCXX::android_content_pm_PackageManager const& arg0);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_content_pm_PermissionInfo