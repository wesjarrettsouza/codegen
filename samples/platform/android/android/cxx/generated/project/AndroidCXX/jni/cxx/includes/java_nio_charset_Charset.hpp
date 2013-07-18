/*
 * Header (Abstract CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



		
 			
		
 			
		
 			
 			
 			
		
 			
 			
		
 			
		
		
		
 			
		
		
		


#ifndef _java_nio_charset_Charset
#define _java_nio_charset_Charset




















#include <java_nio_charset_CharsetDecoder.hpp>
#include <java_lang_Object.hpp>
#include <java_nio_charset_CharsetEncoder.hpp>
#include <java_util_Locale.hpp>
#include <java_nio_CharBuffer.hpp>
#include <java_nio_ByteBuffer.hpp>
#include <java_util_SortedMap.hpp>
#include <java_lang_String.hpp>
#include <java_util_Set.hpp>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace AndroidCXX {

class java_nio_charset_Charset
{
public:
 java_lang_String name();
static java_nio_charset_Charset forName(java_lang_String& arg0);
 bool equals(java_lang_Object& arg0);
 java_lang_String toString();
 int hashCode();
 int compareTo(java_nio_charset_Charset& arg0);
 bool contains(java_nio_charset_Charset& arg0);
 java_nio_CharBuffer decode(java_nio_ByteBuffer& arg0);
 java_nio_ByteBuffer encode(java_nio_CharBuffer& arg0,java_lang_String& arg1);
static bool isSupported(java_lang_String& arg0);
static java_nio_charset_Charset defaultCharset();
 java_util_Set aliases();
static java_util_SortedMap availableCharsets();
 java_lang_String displayName(java_util_Locale& arg0);
 bool isRegistered();
 java_nio_charset_CharsetDecoder newDecoder();
 java_nio_charset_CharsetEncoder newEncoder();
 bool canEncode();


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _java_nio_charset_Charset