/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



		
 			
 			
		
		


#ifndef _android_view_animation_Transformation
#define _android_view_animation_Transformation












#include <android_graphics_Matrix.hpp>
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

class android_view_animation_Transformation
{
public:
 java_lang_String toString();
 void clear();
 void set(android_view_animation_Transformation& arg0);
 void compose(android_view_animation_Transformation& arg0);
 android_graphics_Matrix getMatrix();
 float getAlpha();
 void setAlpha(float& arg0);
 java_lang_String toShortString();
 int getTransformationType();
 void setTransformationType(int& arg0);


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_view_animation_Transformation