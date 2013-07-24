/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


 		 
 		 


 		 
 		 
 		 















// Generated Code 

#ifndef _android_widget_ViewFlipper
#define _android_widget_ViewFlipper
//
// Scroll Down 
//


#include <android_view_accessibility_AccessibilityEvent.hpp>

#include <android_view_accessibility_AccessibilityNodeInfo.hpp>

#include <android_content_Context.hpp>

#include <android_util_AttributeSet.hpp>

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

class android_view_accessibility_AccessibilityEvent;

class android_view_accessibility_AccessibilityNodeInfo;

class android_content_Context;

class android_util_AttributeSet;

class android_widget_ViewFlipper
{
public:

	android_widget_ViewFlipper(const android_widget_ViewFlipper& cc);
	android_widget_ViewFlipper(void * proxy);
	// Public Constructors
	android_widget_ViewFlipper(AndroidCXX::android_content_Context& arg0);
	android_widget_ViewFlipper(AndroidCXX::android_content_Context& arg0,AndroidCXX::android_util_AttributeSet& arg1);
	// TODO: remove
	// 
	// android_widget_ViewFlipper();
	// 
	// Default Destructor
	virtual ~android_widget_ViewFlipper();
	// Functions
	 void onInitializeAccessibilityEvent(AndroidCXX::android_view_accessibility_AccessibilityEvent& arg0);
	 void onInitializeAccessibilityNodeInfo(AndroidCXX::android_view_accessibility_AccessibilityNodeInfo& arg0);
	 void setFlipInterval(int& arg0);
	 void startFlipping();
	 void stopFlipping();
	 bool isFlipping();
	 void setAutoStart(bool& arg0);
	 bool isAutoStart();
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_widget_ViewFlipper