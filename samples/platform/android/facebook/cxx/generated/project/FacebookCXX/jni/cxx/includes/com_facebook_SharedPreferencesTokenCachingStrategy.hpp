/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



	
 		 


 		 
 		 
 		 










// Generated Code 

#ifndef _com_facebook_SharedPreferencesTokenCachingStrategy
#define _com_facebook_SharedPreferencesTokenCachingStrategy
//
// Scroll Down 
//


#include <android_os_Bundle.hpp>

#include <android_content_Context.hpp>

#include <java_lang_String.hpp>

#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>
#include <CXXTypes.hpp>


#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace FacebookCXX {

// Forward Declarations




class com_facebook_SharedPreferencesTokenCachingStrategy
{
public:

	com_facebook_SharedPreferencesTokenCachingStrategy(const com_facebook_SharedPreferencesTokenCachingStrategy& cc);
	com_facebook_SharedPreferencesTokenCachingStrategy(void * proxy);
	// Public Constructors
	com_facebook_SharedPreferencesTokenCachingStrategy(AndroidCXX::android_content_Context& arg0);
	com_facebook_SharedPreferencesTokenCachingStrategy(AndroidCXX::android_content_Context& arg0,AndroidCXX::java_lang_String& arg1);
	com_facebook_SharedPreferencesTokenCachingStrategy();
	// Default Destructor
	virtual ~com_facebook_SharedPreferencesTokenCachingStrategy();
	// Functions
	 void clear();
	 AndroidCXX::android_os_Bundle load();
	 void save(AndroidCXX::android_os_Bundle& arg0);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _com_facebook_SharedPreferencesTokenCachingStrategy