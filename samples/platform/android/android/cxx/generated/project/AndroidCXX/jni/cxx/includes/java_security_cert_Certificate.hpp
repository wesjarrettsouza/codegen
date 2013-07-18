/*
 * Header (Abstract CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
		
		
 			
 			
		


#ifndef _java_security_cert_Certificate
#define _java_security_cert_Certificate









#include <java_security_PublicKey.hpp>
#include <java_lang_Object.hpp>
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

class java_security_cert_Certificate
{
public:
 bool equals(java_lang_Object& arg0);
 java_lang_String toString();
 int hashCode();
 java_lang_String getType();
 std::vector<char> getEncoded();
 void verify(java_security_PublicKey& arg0,java_lang_String& arg1);
 java_security_PublicKey getPublicKey();


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _java_security_cert_Certificate