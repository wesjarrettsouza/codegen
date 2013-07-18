/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 			
		
 			
 			
		
		
 			


#ifndef _java_lang_Double
#define _java_lang_Double





















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

class java_lang_Double
{
public:
 bool equals(java_lang_Object& arg0);
static java_lang_String toString(double& arg0);
 int hashCode();
static long doubleToRawLongBits(double& arg0);
static long doubleToLongBits(double& arg0);
static double longBitsToDouble(long& arg0);
 int compareTo(java_lang_Double& arg0);
 unsigned char byteValue();
 short shortValue();
 int intValue();
 long longValue();
 float floatValue();
 double doubleValue();
static java_lang_Double valueOf(java_lang_String& arg0,double& arg1);
static java_lang_String toHexString(double& arg0);
static int compare(double& arg0);
static bool isNaN(double& arg0);
static bool isInfinite(double& arg0);
static double parseDouble(java_lang_String& arg0);


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _java_lang_Double