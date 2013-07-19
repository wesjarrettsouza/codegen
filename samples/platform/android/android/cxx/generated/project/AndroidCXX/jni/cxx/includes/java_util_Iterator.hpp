/*
 * Header (Callback CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



		


#ifndef _java_util_Iterator
#define _java_util_Iterator





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

class java_util_Iterator
{
public:
	bool hasNext();
	java_lang_Object next();
	void remove();


};

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _java_util_Iterator