/*
 * Header (Abstract CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
		
 			
		
 			
		
		
		
		
		
		
		


#ifndef _java_nio_IntBuffer
#define _java_nio_IntBuffer



















#include <java_nio_ByteOrder.hpp>
#include <java_lang_String.hpp>
#include <java_lang_Object.hpp>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace AndroidCXX {

class java_nio_IntBuffer
{
public:
 int get(std::vector<int>& arg0,int& arg1);
 java_nio_IntBuffer put(java_nio_IntBuffer& arg0,int& arg1,std::vector<int>& arg2);
 bool equals(java_lang_Object& arg0);
 java_lang_String toString();
 int hashCode();
 int compareTo(java_nio_IntBuffer& arg0);
 bool isDirect();
 bool hasArray();
 std::vector<int> array();
 int arrayOffset();
static java_nio_IntBuffer wrap(std::vector<int>& arg0,int& arg1);
static java_nio_IntBuffer allocate(int& arg0);
 java_nio_IntBuffer duplicate();
 java_nio_IntBuffer slice();
 java_nio_IntBuffer asReadOnlyBuffer();
 java_nio_IntBuffer compact();
 java_nio_ByteOrder order();


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _java_nio_IntBuffer