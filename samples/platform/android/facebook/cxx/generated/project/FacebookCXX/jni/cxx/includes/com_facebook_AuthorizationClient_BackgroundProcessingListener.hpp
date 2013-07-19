/*
 * Header (CXX)
 * Author: cxx-bindings-generator
 */

#ifndef _com_facebook_AuthorizationClient_BackgroundProcessingListener
#define _com_facebook_AuthorizationClient_BackgroundProcessingListener

//includes go here

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace FacebookCXX {

class com_facebook_AuthorizationClient_BackgroundProcessingListener
{
public:

	void onBackgroundProcessingStarted();
	void onBackgroundProcessingStopped();


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _com_facebook_AuthorizationClient_BackgroundProcessingListener