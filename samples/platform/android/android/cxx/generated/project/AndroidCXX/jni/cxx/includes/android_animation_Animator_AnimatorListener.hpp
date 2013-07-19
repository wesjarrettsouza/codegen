/*
 * Header (Callback CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
 			
 			
 			


#ifndef _android_animation_Animator_AnimatorListener
#define _android_animation_Animator_AnimatorListener






#include <android_animation_Animator.hpp>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace AndroidCXX {

class android_animation_Animator_AnimatorListener
{
public:
	void onAnimationStart(android_animation_Animator& arg0);
	void onAnimationEnd(android_animation_Animator& arg0);
	void onAnimationRepeat(android_animation_Animator& arg0);
	void onAnimationCancel(android_animation_Animator& arg0);


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_animation_Animator_AnimatorListener