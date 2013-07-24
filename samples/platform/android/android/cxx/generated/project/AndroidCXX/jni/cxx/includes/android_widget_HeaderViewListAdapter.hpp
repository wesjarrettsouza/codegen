/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


 		 
 		 
	
	
	
 		 
 		 
	
 		 
 		 


 		 
 	
 		 
 	
 		 
 		 
 		 
























// Generated Code 

#ifndef _android_widget_HeaderViewListAdapter
#define _android_widget_HeaderViewListAdapter
//
// Scroll Down 
//


#include <android_view_View.hpp>

#include <android_view_ViewGroup.hpp>

#include <android_widget_Filter.hpp>

#include <java_lang_Object.hpp>

#include <android_database_DataSetObserver.hpp>

#include <android_widget_ListAdapter.hpp>

#include <java_util_ArrayList.hpp>

#include <android_widget_ListView_FixedViewInfo.hpp>

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

class android_view_View;

class android_view_ViewGroup;

class android_widget_Filter;

class java_lang_Object;

class android_database_DataSetObserver;

class android_widget_ListAdapter;

class java_util_ArrayList;

class android_widget_ListView_FixedViewInfo;

class android_widget_HeaderViewListAdapter
{
public:

	android_widget_HeaderViewListAdapter(const android_widget_HeaderViewListAdapter& cc);
	android_widget_HeaderViewListAdapter(void * proxy);
	// Public Constructors
	android_widget_HeaderViewListAdapter(AndroidCXX::java_util_ArrayList& arg0,AndroidCXX::java_util_ArrayList& arg1,AndroidCXX::android_widget_ListAdapter& arg2);
	// TODO: remove
	// 
	// android_widget_HeaderViewListAdapter();
	// 
	// Default Destructor
	virtual ~android_widget_HeaderViewListAdapter();
	// Functions
	 bool isEmpty();
	 AndroidCXX::android_view_View getView(int& arg0,AndroidCXX::android_view_View& arg1,AndroidCXX::android_view_ViewGroup& arg2);
	 bool isEnabled(int& arg0);
	 AndroidCXX::android_widget_Filter getFilter();
	 AndroidCXX::java_lang_Object getItem(int& arg0);
	 long getItemId(int& arg0);
	 int getCount();
	 void registerDataSetObserver(AndroidCXX::android_database_DataSetObserver& arg0);
	 void unregisterDataSetObserver(AndroidCXX::android_database_DataSetObserver& arg0);
	 bool hasStableIds();
	 int getItemViewType(int& arg0);
	 int getViewTypeCount();
	 bool areAllItemsEnabled();
	 AndroidCXX::android_widget_ListAdapter getWrappedAdapter();
	 int getHeadersCount();
	 int getFootersCount();
	 bool removeHeader(AndroidCXX::android_view_View& arg0);
	 bool removeFooter(AndroidCXX::android_view_View& arg0);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_widget_HeaderViewListAdapter