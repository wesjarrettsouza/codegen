/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



		
 			
		
 			
		
 			


#ifndef _android_widget_TextClock
#define _android_widget_TextClock









#include <java_lang_CharSequence.hpp>
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

class android_widget_TextClock
{
public:
 java_lang_String getTimeZone();
 void setTimeZone(java_lang_String& arg0);
 java_lang_CharSequence getFormat12Hour();
 void setFormat12Hour(java_lang_CharSequence& arg0);
 java_lang_CharSequence getFormat24Hour();
 void setFormat24Hour(java_lang_CharSequence& arg0);
 bool is24HourModeEnabled();


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_widget_TextClock