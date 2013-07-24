/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


 		 
 		 
 		 
 		 
 		 
 		 
 		 
 		 
 		 
 		 
 		 
 		 
 		 
























// Generated Code 

#ifndef _android_view_ViewTreeObserver
#define _android_view_ViewTreeObserver
//
// Scroll Down 
//


#include <android_view_ViewTreeObserver_OnGlobalFocusChangeListener.hpp>

#include <android_view_ViewTreeObserver_OnGlobalLayoutListener.hpp>

#include <android_view_ViewTreeObserver_OnPreDrawListener.hpp>

#include <android_view_ViewTreeObserver_OnDrawListener.hpp>

#include <android_view_ViewTreeObserver_OnScrollChangedListener.hpp>

#include <android_view_ViewTreeObserver_OnTouchModeChangeListener.hpp>

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

class android_view_ViewTreeObserver_OnGlobalFocusChangeListener;

class android_view_ViewTreeObserver_OnGlobalLayoutListener;

class android_view_ViewTreeObserver_OnPreDrawListener;

class android_view_ViewTreeObserver_OnDrawListener;

class android_view_ViewTreeObserver_OnScrollChangedListener;

class android_view_ViewTreeObserver_OnTouchModeChangeListener;

class android_view_ViewTreeObserver
{
public:

	android_view_ViewTreeObserver(const android_view_ViewTreeObserver& cc);
	android_view_ViewTreeObserver(void * proxy);
	// Public Constructors
	// TODO: remove
	// 
	// android_view_ViewTreeObserver();
	// 
	// Default Destructor
	virtual ~android_view_ViewTreeObserver();
	// Functions
	 bool isAlive();
	 void addOnGlobalFocusChangeListener(AndroidCXX::android_view_ViewTreeObserver_OnGlobalFocusChangeListener& arg0);
	 void removeOnGlobalFocusChangeListener(AndroidCXX::android_view_ViewTreeObserver_OnGlobalFocusChangeListener& arg0);
	 void addOnGlobalLayoutListener(AndroidCXX::android_view_ViewTreeObserver_OnGlobalLayoutListener& arg0);
	 void removeGlobalOnLayoutListener(AndroidCXX::android_view_ViewTreeObserver_OnGlobalLayoutListener& arg0);
	 void removeOnGlobalLayoutListener(AndroidCXX::android_view_ViewTreeObserver_OnGlobalLayoutListener& arg0);
	 void addOnPreDrawListener(AndroidCXX::android_view_ViewTreeObserver_OnPreDrawListener& arg0);
	 void removeOnPreDrawListener(AndroidCXX::android_view_ViewTreeObserver_OnPreDrawListener& arg0);
	 void addOnDrawListener(AndroidCXX::android_view_ViewTreeObserver_OnDrawListener& arg0);
	 void removeOnDrawListener(AndroidCXX::android_view_ViewTreeObserver_OnDrawListener& arg0);
	 void addOnScrollChangedListener(AndroidCXX::android_view_ViewTreeObserver_OnScrollChangedListener& arg0);
	 void removeOnScrollChangedListener(AndroidCXX::android_view_ViewTreeObserver_OnScrollChangedListener& arg0);
	 void addOnTouchModeChangeListener(AndroidCXX::android_view_ViewTreeObserver_OnTouchModeChangeListener& arg0);
	 void removeOnTouchModeChangeListener(AndroidCXX::android_view_ViewTreeObserver_OnTouchModeChangeListener& arg0);
	 void dispatchOnGlobalLayout();
	 bool dispatchOnPreDraw();
	 void dispatchOnDraw();
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_view_ViewTreeObserver