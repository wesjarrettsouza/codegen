/*
 * Header (Instance CXX)
 * Author: cxx-bindings-generator
 */

//
// Scroll Down 
//



 		 
	
	
 	
 		 
 		 
 	
 		 


 		 
 	
 		 
 		 
 	
 		 














// Generated Code 

#ifndef _java_security_CodeSource
#define _java_security_CodeSource
//
// Scroll Down 
//


#include <java_lang_Object.hpp>

#include <java_lang_String.hpp>

#include <java_net_URL.hpp>

#include <java_security_cert_Certificate.hpp>


#include <java_security_CodeSigner.hpp>

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

class java_lang_Object;

class java_lang_String;

class java_net_URL;

class java_security_cert_Certificate;

class java_security_CodeSource;

class java_security_CodeSigner;

class java_security_CodeSource
{
public:

	java_security_CodeSource(const java_security_CodeSource& cc);
	java_security_CodeSource(void * proxy);
	// Public Constructors
	java_security_CodeSource(JDKCXX::java_net_URL& arg0,std::vector<JDKCXX::java_security_CodeSigner >& arg1);
	java_security_CodeSource(JDKCXX::java_net_URL& arg0,std::vector<JDKCXX::java_security_cert_Certificate >& arg1);
	// TODO: remove
	// 
	// java_security_CodeSource();
	// 
	// Default Destructor
	virtual ~java_security_CodeSource();
	// Functions
	 bool equals(JDKCXX::java_lang_Object& arg0);
	 JDKCXX::java_lang_String toString();
	 int hashCode();
	 JDKCXX::java_net_URL getLocation();
	 std::vector<JDKCXX::java_security_cert_Certificate > getCertificates();
	 bool implies(JDKCXX::java_security_CodeSource& arg0);
	 std::vector<JDKCXX::java_security_CodeSigner > getCodeSigners();
};	

} // namespace

#ifdef __cplusplus
}
#endif //__cplusplus

#endif // _java_security_CodeSource