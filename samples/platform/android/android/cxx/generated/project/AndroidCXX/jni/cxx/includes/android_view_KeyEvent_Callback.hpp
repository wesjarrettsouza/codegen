/*
 * Header (Callback CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
 			
 			
 			


#ifndef _android_view_KeyEvent_Callback
#define _android_view_KeyEvent_Callback






#include <android_view_KeyEvent.hpp>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace AndroidCXX {

class android_view_KeyEvent_Callback
{
public:
	bool onKeyDown(int& arg0,android_view_KeyEvent& arg1);
	bool onKeyLongPress(int& arg0,android_view_KeyEvent& arg1);
	bool onKeyUp(int& arg0,android_view_KeyEvent& arg1);
	bool onKeyMultiple(int& arg0,android_view_KeyEvent& arg1);


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_view_KeyEvent_Callback