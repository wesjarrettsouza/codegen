/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


	
 		 
 		 
 		 
 		 
 		 


 		 
 		 
 		 
 		 
 		 






















// Generated Code 

#ifndef _android_widget_CompoundButton
#define _android_widget_CompoundButton
//
// Scroll Down 
//


#include <android_os_Parcelable.hpp>

#include <android_view_accessibility_AccessibilityEvent.hpp>

#include <android_view_accessibility_AccessibilityNodeInfo.hpp>

#include <android_widget_CompoundButton_OnCheckedChangeListener.hpp>

#include <android_graphics_drawable_Drawable.hpp>

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

class android_os_Parcelable;

class android_view_accessibility_AccessibilityEvent;

class android_view_accessibility_AccessibilityNodeInfo;

class android_widget_CompoundButton_OnCheckedChangeListener;

class android_graphics_drawable_Drawable;

class android_content_Context;

class android_util_AttributeSet;

class android_widget_CompoundButton
{
public:

	android_widget_CompoundButton(const android_widget_CompoundButton& cc);
	android_widget_CompoundButton(void * proxy);
	// Public Constructors
	android_widget_CompoundButton(AndroidCXX::android_content_Context& arg0,AndroidCXX::android_util_AttributeSet& arg1);
	android_widget_CompoundButton(AndroidCXX::android_content_Context& arg0,AndroidCXX::android_util_AttributeSet& arg1,int& arg2);
	android_widget_CompoundButton(AndroidCXX::android_content_Context& arg0);
	// TODO: remove
	// 
	// android_widget_CompoundButton();
	// 
	// Default Destructor
	virtual ~android_widget_CompoundButton();
	// Functions
	 AndroidCXX::android_os_Parcelable onSaveInstanceState();
	 void onRestoreInstanceState(AndroidCXX::android_os_Parcelable& arg0);
	 void jumpDrawablesToCurrentState();
	 bool performClick();
	 void onInitializeAccessibilityEvent(AndroidCXX::android_view_accessibility_AccessibilityEvent& arg0);
	 void onInitializeAccessibilityNodeInfo(AndroidCXX::android_view_accessibility_AccessibilityNodeInfo& arg0);
	 void setChecked(bool& arg0);
	 bool isChecked();
	 void toggle();
	 int getCompoundPaddingLeft();
	 int getCompoundPaddingRight();
	 void setOnCheckedChangeListener(AndroidCXX::android_widget_CompoundButton_OnCheckedChangeListener& arg0);
	 void setButtonDrawable(AndroidCXX::android_graphics_drawable_Drawable& arg0);
	 void setButtonDrawable(int& arg0);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_widget_CompoundButton