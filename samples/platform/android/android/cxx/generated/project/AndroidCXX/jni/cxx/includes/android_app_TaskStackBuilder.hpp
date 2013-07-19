/*
 * Header (Abstract CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
		
 			
 			
		
 			
		
 			
 			
 			
		
		
 			
		


#ifndef _android_app_TaskStackBuilder
#define _android_app_TaskStackBuilder











#include <android_content_ComponentName.hpp>
#include <java_lang_Class.hpp>
#include <android_content_Context.hpp>
#include <android_os_Bundle.hpp>
#include <android_content_Intent.hpp>
#include <android_app_PendingIntent.hpp>
#include <android_app_Activity.hpp>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace AndroidCXX {

class android_app_TaskStackBuilder
{
public:
static android_app_TaskStackBuilder create(android_content_Context& arg0);
 void startActivities(android_os_Bundle& arg0);
 android_app_TaskStackBuilder addNextIntent(android_content_Intent& arg0);
 android_app_TaskStackBuilder addNextIntentWithParentStack(android_content_Intent& arg0);
 android_app_TaskStackBuilder addParentStack(android_app_Activity& arg0,java_lang_Class& arg1,android_content_ComponentName& arg2);
 int getIntentCount();
 android_content_Intent editIntentAt(int& arg0);
 android_app_PendingIntent getPendingIntent(int& arg0,android_os_Bundle& arg1);
 std::vector<long> getIntents();


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_app_TaskStackBuilder