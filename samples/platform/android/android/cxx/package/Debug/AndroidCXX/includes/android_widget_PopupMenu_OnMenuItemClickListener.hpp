/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


 		 








// Generated Code 

#ifndef _android_widget_PopupMenu_OnMenuItemClickListener
#define _android_widget_PopupMenu_OnMenuItemClickListener
//
// Scroll Down 
//


#include <android_view_MenuItem.hpp>

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

class android_view_MenuItem;

class android_widget_PopupMenu_OnMenuItemClickListener
{
public:

	android_widget_PopupMenu_OnMenuItemClickListener(const android_widget_PopupMenu_OnMenuItemClickListener& cc);
	android_widget_PopupMenu_OnMenuItemClickListener(Proxy proxy);
	// Public Constructors
	Proxy proxy() const;	
	// Default Destructor
	virtual ~android_widget_PopupMenu_OnMenuItemClickListener();
	// Functions
	 bool onMenuItemClick(AndroidCXX::android_view_MenuItem const& arg0);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_widget_PopupMenu_OnMenuItemClickListener