/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


 		 
	
 		 
 		 


 		 


















// Generated Code 

#ifndef _android_graphics_Point
#define _android_graphics_Point
//
// Scroll Down 
//


#include <java_lang_Object.hpp>

#include <java_lang_String.hpp>

#include <android_os_Parcel.hpp>


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

class java_lang_Object;

class java_lang_String;

class android_os_Parcel;

class android_graphics_Point;

class android_graphics_Point
{
public:

	android_graphics_Point(const android_graphics_Point& cc);
	android_graphics_Point(void * proxy);
	// Public Constructors
	android_graphics_Point();
	android_graphics_Point(int& arg0,int& arg1);
	android_graphics_Point(AndroidCXX::android_graphics_Point& arg0);
	// TODO: remove
	// 
	// Default Destructor
	virtual ~android_graphics_Point();
	// Functions
	 bool equals(int& arg0,int& arg1);
	 bool equals(AndroidCXX::java_lang_Object& arg0);
	 AndroidCXX::java_lang_String toString();
	 int hashCode();
	 void offset(int& arg0,int& arg1);
	 void set(int& arg0,int& arg1);
	 void negate();
	 int describeContents();
	 void writeToParcel(AndroidCXX::android_os_Parcel& arg0,int& arg1);
	 void readFromParcel(AndroidCXX::android_os_Parcel& arg0);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_graphics_Point