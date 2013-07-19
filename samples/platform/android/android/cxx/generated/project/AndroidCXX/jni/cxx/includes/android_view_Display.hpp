/*
 * Header (Abstract CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



		
		
 			
 			
 			
 			
 			
 			


#ifndef _android_view_Display
#define _android_view_Display



















#include <android_graphics_Point.hpp>
#include <android_graphics_Rect.hpp>
#include <android_util_DisplayMetrics.hpp>
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

class android_view_Display
{
public:
 java_lang_String toString();
 java_lang_String getName();
 void getSize(android_graphics_Point& arg0);
 bool isValid();
 int getFlags();
 int getWidth();
 int getHeight();
 int getRotation();
 int getDisplayId();
 void getRectSize(android_graphics_Rect& arg0);
 void getCurrentSizeRange(android_graphics_Point& arg0);
 int getOrientation();
 int getPixelFormat();
 float getRefreshRate();
 void getMetrics(android_util_DisplayMetrics& arg0);
 void getRealSize(android_graphics_Point& arg0);
 void getRealMetrics(android_util_DisplayMetrics& arg0);


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_view_Display