/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
		
 			
 			
 			
 			
 			
 			
		
		
 			
		
 			
 			


#ifndef _android_graphics_Rect
#define _android_graphics_Rect





























#include <android_os_Parcel.hpp>
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

class android_graphics_Rect
{
public:
 bool equals(java_lang_Object& arg0);
 java_lang_String toString();
 int hashCode();
 void offset(int& arg0);
 bool isEmpty();
 bool contains(android_graphics_Rect& arg0,int& arg1);
 void set(int& arg0,android_graphics_Rect& arg1);
 void sort();
static bool intersects(int& arg0,android_graphics_Rect& arg1);
 void union(int& arg0,android_graphics_Rect& arg1);
 int describeContents();
 void writeToParcel(android_os_Parcel& arg0,int& arg1);
 void readFromParcel(android_os_Parcel& arg0);
 int width();
 int height();
 java_lang_String toShortString();
 java_lang_String flattenToString();
static android_graphics_Rect unflattenFromString(java_lang_String& arg0);
 int centerX();
 int centerY();
 float exactCenterX();
 float exactCenterY();
 void setEmpty();
 void offsetTo(int& arg0);
 void inset(int& arg0);
 bool intersect(android_graphics_Rect& arg0,int& arg1);
 bool setIntersect(android_graphics_Rect& arg0);


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_graphics_Rect