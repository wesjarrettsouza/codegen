/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



		
		
 			
 			
 			
 			
 			
 			
 			
		
 			
 			


#ifndef _android_content_Loader
#define _android_content_Loader
























#include <java_io_PrintWriter.hpp>
#include <java_lang_Object.hpp>
#include <android_content_Context.hpp>
#include <android_content_Loader_OnLoadCompleteListener.hpp>
#include <android_content_Loader_OnLoadCanceledListener.hpp>
#include <java_io_FileDescriptor.hpp>
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

class android_content_Loader
{
public:
 java_lang_String toString();
 android_content_Context getContext();
 int getId();
 void reset();
 void dump(java_lang_String& arg0,java_io_FileDescriptor& arg1,java_io_PrintWriter& arg2,std::vector<long>& arg3);
 void abandon();
 void onContentChanged();
 bool isStarted();
 void deliverResult(java_lang_Object& arg0);
 void registerListener(int& arg0,android_content_Loader_OnLoadCompleteListener& arg1);
 void unregisterListener(android_content_Loader_OnLoadCompleteListener& arg0);
 bool isAbandoned();
 bool isReset();
 void startLoading();
 void forceLoad();
 void stopLoading();
 bool takeContentChanged();
 java_lang_String dataToString(java_lang_Object& arg0);
 void deliverCancellation();
 void registerOnLoadCanceledListener(android_content_Loader_OnLoadCanceledListener& arg0);
 void unregisterOnLoadCanceledListener(android_content_Loader_OnLoadCanceledListener& arg0);
 bool cancelLoad();


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_content_Loader