/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
 			
		
 			
 			
 			
 			
 			
 			
 			
 			


#ifndef _android_content_res_Configuration
#define _android_content_res_Configuration


















#include <android_os_Parcel.hpp>
#include <java_util_Locale.hpp>
#include <java_lang_Object.hpp>
#include <java_lang_String.hpp>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace AndroidCXX {

class android_content_res_Configuration
{
public:
 bool equals(android_content_res_Configuration& arg0,java_lang_Object& arg1);
 java_lang_String toString();
 int hashCode();
 int compareTo(android_content_res_Configuration& arg0);
 void setLocale(java_util_Locale& arg0);
 int describeContents();
 void writeToParcel(android_os_Parcel& arg0,int& arg1);
 void readFromParcel(android_os_Parcel& arg0);
 void setLayoutDirection(java_util_Locale& arg0);
 int getLayoutDirection();
 bool isLayoutSizeAtLeast(int& arg0);
 void setTo(android_content_res_Configuration& arg0);
 void setToDefaults();
 int updateFrom(android_content_res_Configuration& arg0);
 int diff(android_content_res_Configuration& arg0);
static bool needNewResources(int& arg0);


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_content_res_Configuration