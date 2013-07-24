/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//


 	
	
 	
	
 		 
	
	
	
 	
	
 	
	
 		 
	
 		 
 	
 	
	
 	
	
	
	
	
	
	
	
































// Generated Code 

#ifndef _java_nio_IntBuffer
#define _java_nio_IntBuffer
//
// Scroll Down 
//



#include <java_lang_Object.hpp>

#include <java_lang_String.hpp>

#include <java_nio_ByteOrder.hpp>

#include <vector>
#include <map>
#include <string>
#include <stack>
#include <list>
#include <CXXTypes.hpp>


#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

namespace JDKCXX {

// Forward Declarations

class java_nio_IntBuffer;

class java_lang_Object;

class java_lang_String;

class java_nio_ByteOrder;

class java_nio_IntBuffer
{
public:

	java_nio_IntBuffer(const java_nio_IntBuffer& cc);
	java_nio_IntBuffer(void * proxy);
	// Public Constructors
	// TODO: remove
	// 
	// java_nio_IntBuffer();
	// 
	// Default Destructor
	virtual ~java_nio_IntBuffer();
	// Functions
	 int get();
	 JDKCXX::java_nio_IntBuffer get(std::vector<int>& arg0);
	 JDKCXX::java_nio_IntBuffer get(std::vector<int>& arg0,int& arg1,int& arg2);
	 int get(int& arg0);
	 JDKCXX::java_nio_IntBuffer put(JDKCXX::java_nio_IntBuffer& arg0);
	 JDKCXX::java_nio_IntBuffer put(int& arg0);
	 JDKCXX::java_nio_IntBuffer put(int& arg0,int& arg1);
	 JDKCXX::java_nio_IntBuffer put(std::vector<int>& arg0,int& arg1,int& arg2);
	 JDKCXX::java_nio_IntBuffer put(std::vector<int>& arg0);
	 bool equals(JDKCXX::java_lang_Object& arg0);
	 JDKCXX::java_lang_String toString();
	 int hashCode();
	 int compareTo(JDKCXX::java_nio_IntBuffer& arg0);
	 bool isDirect();
	 bool hasArray();
	 std::vector<int> array();
	 int arrayOffset();
	static JDKCXX::java_nio_IntBuffer wrap(std::vector<int>& arg0,int& arg1,int& arg2);
	static JDKCXX::java_nio_IntBuffer wrap(std::vector<int>& arg0);
	static JDKCXX::java_nio_IntBuffer allocate(int& arg0);
	 JDKCXX::java_nio_IntBuffer duplicate();
	 JDKCXX::java_nio_IntBuffer slice();
	 JDKCXX::java_nio_IntBuffer asReadOnlyBuffer();
	 JDKCXX::java_nio_IntBuffer compact();
	 JDKCXX::java_nio_ByteOrder order();
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _java_nio_IntBuffer