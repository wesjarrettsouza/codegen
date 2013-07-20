/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 		 
 		 
 		 
 		 
	

// Generated Code 

#ifndef _android_widget_BaseAdapter
#define _android_widget_BaseAdapter
//
// Scroll Down 
//














#include <android_database_DataSetObserver.hpp>

#include <android_view_View.hpp>

#include <android_view_ViewGroup.hpp>

#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace AndroidCXX {

// Forward Declarations

class android_database_DataSetObserver;

class android_view_View;

class android_view_ViewGroup;

class android_widget_BaseAdapter
{
public:
	 bool isEmpty();
	 bool isEnabled(int& arg0);
	 void registerDataSetObserver(android_database_DataSetObserver& arg0);
	 void unregisterDataSetObserver(android_database_DataSetObserver& arg0);
	 android_view_View *  getDropDownView(int& arg0,android_view_View& arg1,android_view_ViewGroup& arg2);
	 bool hasStableIds();
	 int getItemViewType(int& arg0);
	 int getViewTypeCount();
	 bool areAllItemsEnabled();
	 void notifyDataSetChanged();
	 void notifyDataSetInvalidated();
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_widget_BaseAdapter