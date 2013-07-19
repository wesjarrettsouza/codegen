/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
 			
		
		
 			


#ifndef _android_webkit_WebChromeClient
#define _android_webkit_WebChromeClient
























#include <android_webkit_ValueCallback.hpp>
#include <android_webkit_JsPromptResult.hpp>
#include <android_webkit_WebView.hpp>
#include <android_os_Message.hpp>
#include <android_graphics_Bitmap.hpp>
#include <android_webkit_GeolocationPermissions_Callback.hpp>
#include <android_webkit_ConsoleMessage.hpp>
#include <android_webkit_JsResult.hpp>
#include <android_view_View.hpp>
#include <android_webkit_WebStorage_QuotaUpdater.hpp>
#include <android_webkit_WebChromeClient_CustomViewCallback.hpp>
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

class android_webkit_WebChromeClient
{
public:
 void onProgressChanged(android_webkit_WebView& arg0,int& arg1);
 void onReceivedTitle(android_webkit_WebView& arg0,java_lang_String& arg1);
 void onReceivedIcon(android_webkit_WebView& arg0,android_graphics_Bitmap& arg1);
 void onReceivedTouchIconUrl(android_webkit_WebView& arg0,java_lang_String& arg1,bool& arg2);
 void onShowCustomView(android_view_View& arg0,android_webkit_WebChromeClient_CustomViewCallback& arg1,int& arg2);
 void onHideCustomView();
 bool onCreateWindow(android_webkit_WebView& arg0,bool& arg1,android_os_Message& arg2);
 void onRequestFocus(android_webkit_WebView& arg0);
 void onCloseWindow(android_webkit_WebView& arg0);
 bool onJsAlert(android_webkit_WebView& arg0,java_lang_String& arg1,android_webkit_JsResult& arg2);
 bool onJsConfirm(android_webkit_WebView& arg0,java_lang_String& arg1,android_webkit_JsResult& arg2);
 bool onJsPrompt(android_webkit_WebView& arg0,java_lang_String& arg1,android_webkit_JsPromptResult& arg2);
 bool onJsBeforeUnload(android_webkit_WebView& arg0,java_lang_String& arg1,android_webkit_JsResult& arg2);
 void onExceededDatabaseQuota(java_lang_String& arg0,long& arg1,android_webkit_WebStorage_QuotaUpdater& arg2);
 void onReachedMaxAppCacheSize(long& arg0,android_webkit_WebStorage_QuotaUpdater& arg1);
 void onGeolocationPermissionsShowPrompt(java_lang_String& arg0,android_webkit_GeolocationPermissions_Callback& arg1);
 void onGeolocationPermissionsHidePrompt();
 bool onJsTimeout();
 void onConsoleMessage(java_lang_String& arg0,int& arg1,android_webkit_ConsoleMessage& arg2);
 android_graphics_Bitmap getDefaultVideoPoster();
 android_view_View getVideoLoadingProgressView();
 void getVisitedHistory(android_webkit_ValueCallback& arg0);


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_webkit_WebChromeClient