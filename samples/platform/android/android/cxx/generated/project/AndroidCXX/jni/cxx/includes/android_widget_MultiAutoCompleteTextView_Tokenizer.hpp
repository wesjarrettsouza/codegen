/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 		 
 		 
 		 
	

// Generated Code 

#ifndef _android_widget_MultiAutoCompleteTextView_Tokenizer
#define _android_widget_MultiAutoCompleteTextView_Tokenizer
//
// Scroll Down 
//






#include <java_lang_CharSequence.hpp>

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

class java_lang_CharSequence;

class android_widget_MultiAutoCompleteTextView_Tokenizer
{
public:
	 int findTokenStart(java_lang_CharSequence& arg0,int& arg1);
	 int findTokenEnd(java_lang_CharSequence& arg0,int& arg1);
	 java_lang_CharSequence *  terminateToken(java_lang_CharSequence& arg0);
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _android_widget_MultiAutoCompleteTextView_Tokenizer