#	Enum Tags
#		_proxy 												Tag to indicate enum will be proxied
#		_no_proxy											Tag to indicate enum will not be proxied
#	Protocol Tags
#		_proxy 												Tag to indicate protocol will be proxied
#		_no_proxy											Tag to indicate protocol will not be proxied
#	Interface Tags
#		_proxy 												Tag to indicate interface will be proxied
#		_no_proxy											Tag to indicate interface will not be proxied
#	Method Tags
#		_static												Tag to indicate method is a static method
#		_instance 											Tag to indicate method is an instance method
#		_variadic											Tag to indicate method is a variadic method
#		_proxy 												Tag to indicate method will be proxied
#		_no_proxy											Tag to indicate method will not be proxied


config = {
	'namespace' : 'FacebookCXX',
	'package'	: 'FacebookCXX',
	'converters' : [
		{
			'cxx' : {'type': 'std::string'},
			'objc' : {'type': 'NSString *'},
			'name' : 'convert_string',
		},
		{
			'cxx' : {'type': 'std::string'},
			'objc' : {'type': 'NSError *'},
			'name' : 'convert_error',
		},
		{
			'cxx' : {'type': 'std::vector<void *>'},
			'objc' : {'type': 'NSArray *'},
			'name' : 'convert_array',
		},
		{
			'cxx' : {'type': 'std::map<void *, void *>'},
			'objc' : {'type': 'NSDictionary *'},
			'name' : 'convert_dictionary',
		},
		{
			'cxx' : {'type': 'std::string'},
			'objc' : {'type': 'NSUrl *'},
			'name' : 'convert_url',
		},
		{
			'cxx' : {'type': 'double'},
			'objc' : {'type': 'NSDate *'},
			'name' : 'convert_date',
		},
		{
			'cxx' : {'type': 'std::string'},
			'objc' : {'type': 'NSLocale *'},
			'name' : 'convert_locale',
		},
		{
			'cxx' : {'type': 'void *'},
			'objc' : {'type': 'id'},
			'name' : 'convert_object',
		},
	],
	'frameworks' : [
		'../objc/facebook-ios-sdk/FacebookSDK.framework',
	],
	'enums' : [
		{
			'typedef'	: 'FBProfilePictureCropping',
			'tags'      : ['_proxy'],
			'constants' : [
				{
					'name'  : 'FBProfilePictureCroppingSquare',
					'value' : '0'
				},
				{
					'name'  : 'FBProfilePictureCroppingOriginal',
					'value' : '1'
				},
			]
		},
		{
			'typedef'	: 'FBNativeDialogResult',
			'tags'      : ['_proxy'],
			'constants' : [
				{
					'name'  : 'FBNativeDialogResultSucceeded',
					'value' : '0'
				},
				{
					'name'  : 'FBNativeDialogResultCancelled',
					'value' : '1'
				},
				{
					'name'  : 'FBNativeDialogResultError',
					'value' : '2'
				},
			]
		},
		{
			'typedef'	: 'FBSessionDefaultAudience',
			'tags'      : ['_proxy'],
			'constants' : [
				{
					'name'  : 'FBSessionDefaultAudienceNone',
					'value' : '0'
				},
				{
					'name'  : 'FBSessionDefaultAudienceOnlyMe',
					'value' : '10'
				},
				{
					'name'  : 'FBSessionDefaultAudienceFriends',
					'value' : '20'
				},
				{
					'name'  : 'FBSessionDefaultAudienceEveryone',
					'value' : '30'
				},
			]
		},
		{
			'typedef'	: 'FBSessionState',
			'tags'      : ['_proxy'],
			'constants' : [
				{
					'name'  : 'FBSessionStateCreated',
					'value' : '0'
				},
				{
					'name'  : 'FBSessionStateCreatedTokenLoaded',
					'value' : '1'
				},
				{
					'name'  : 'FBSessionStateCreatedOpening',
					'value' : '2'
				},
				{
					'name'  : 'FBSessionStateOpen',
					'value' : '513'
				},
				{
					'name'  : 'FBSessionStateOpenTokenExtended',
					'value' : '514'
				},
				{
					'name'  : 'FBSessionStateClosedLoginFailed',
					'value' : '257'
				},
				{
					'name'  : 'FBSessionStateClosed',
					'value' : '258'
				},
			]
		},
		{
			'typedef'	: 'FBSessionLoginBehavior',
			'tags'      : ['_proxy'],
			'constants' : [
				{
					'name'  : 'FBSessionLoginBehaviorWithFallbackToWebView',
					'value' : '0'
				},
				{
					'name'  : 'FBSessionLoginBehaviorWithNoFallbackToWebView',
					'value' : '1'
				},
				{
					'name'  : 'FBSessionLoginBehaviorForcingWebView',
					'value' : '2'
				},
				{
					'name'  : 'FBSessionLoginBehaviorUseSystemAccountIfPresent',
					'value' : '3'
				},
			]
		},
		{
			'typedef'	: 'FBSessionLoginType',
			'tags'      : ['_proxy'],
			'constants' : [
				{
					'name'  : 'FBSessionLoginTypeNone',
					'value' : '0'
				},
				{
					'name'  : 'FBSessionLoginTypeSystemAccount',
					'value' : '1'
				},
				{
					'name'  : 'FBSessionLoginTypeFacebookApplication',
					'value' : '2'
				},
				{
					'name'  : 'FBSessionLoginTypeFacebookViaSafari',
					'value' : '3'
				},
				{
					'name'  : 'FBSessionLoginTypeWebView',
					'value' : '4'
				},
				{
					'name'  : 'FBSessionLoginTypeTestUser',
					'value' : '5'
				},
			]
		},
		{
			'typedef'	: 'FBFriendSortOrdering',
			'tags'      : ['_proxy'],
			'constants' : [
				{
					'name'  : 'FBFriendSortByFirstName',
					'value' : '0'
				},
				{
					'name'  : 'FBFriendSortByLastName',
					'value' : '1'
				},
			]
		},
		{
			'typedef'	: 'FBFriendDisplayOrdering',
			'tags'      : ['_proxy'],
			'constants' : [
				{
					'name'  : 'FBFriendDisplayByFirstName',
					'value' : '0'
				},
				{
					'name'  : 'FBFriendDisplayByLastName',
					'value' : '1'
				},
			]
		},
	],
	'interfaces' : [
		{
			'name' : 'FBViewController',
			'file' : 'FBViewController.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'presentModallyFromViewController:animated:handler:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIViewController *',
								'name' : 'viewController',
								'converter' : 'convert_object',
						},
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'animated',
								'converter' : 'convert_builtin',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBModalCompletionHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBViewController *', 'converter': 'convert_proxy'}, {'declared_type': 'BOOL', 'kind': 'Builtin', 'type': 'signed char', 'converter': 'convert_builtin'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBViewController *, signed char)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'cancelButton',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIBarButtonItem *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setCancelButton:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIBarButtonItem *',
								'name' : 'cancelButton',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'doneButton',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIBarButtonItem *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setDoneButton:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIBarButtonItem *',
								'name' : 'doneButton',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'delegate',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'conforms_to' : ['FBViewControllerDelegate'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBViewControllerDelegate>',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setDelegate:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'conforms_to' : ['FBViewControllerDelegate'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBViewControllerDelegate>',
								'name' : 'delegate',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'canvasView',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIView *',
								'converter' : 'convert_object',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBProfilePictureView',
			'file' : 'FBProfilePictureView.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'init',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithProfileID:pictureCropping:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'profileID',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'Enum',
								'type' : 'FBProfilePictureCropping',
								'name' : 'pictureCropping',
								'converter' : 'convert_enum',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'profileID',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setProfileID:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'profileID',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'pictureCropping',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Enum',
								'type' : 'FBProfilePictureCropping',
								'converter' : 'convert_enum',
						},
					],
				},
				{
					'selector' : 'setPictureCropping:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'Enum',
								'type' : 'FBProfilePictureCropping',
								'name' : 'pictureCropping',
								'converter' : 'convert_enum',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBSessionTokenCachingStrategy',
			'file' : 'FBSessionTokenCachingStrategy.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'init',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithUserDefaultTokenInformationKeyName:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'tokenInformationKeyName',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'cacheTokenInformation:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDictionary *',
								'name' : 'tokenInformation',
								'converter' : 'convert_dictionary',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'fetchTokenInformation',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDictionary *',
								'converter' : 'convert_dictionary',
						},
					],
				},
				{
					'selector' : 'clearToken',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'defaultInstance',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSessionTokenCachingStrategy *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'isValidTokenInformation:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDictionary *',
								'name' : 'tokenInformation',
								'converter' : 'convert_dictionary',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBNativeDialogs',
			'file' : 'FBNativeDialogs.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'presentShareDialogModallyFrom:initialText:image:url:handler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIViewController *',
								'name' : 'viewController',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'initialText',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIImage *',
								'name' : 'image',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSURL *',
								'name' : 'url',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBShareDialogHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'Enum', 'type': 'FBNativeDialogResult', 'converter': 'convert_enum'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBNativeDialogResult, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'presentShareDialogModallyFrom:initialText:images:urls:handler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIViewController *',
								'name' : 'viewController',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'initialText',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'images',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'urls',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBShareDialogHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'Enum', 'type': 'FBNativeDialogResult', 'converter': 'convert_enum'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBNativeDialogResult, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'presentShareDialogModallyFrom:session:initialText:images:urls:handler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIViewController *',
								'name' : 'viewController',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'initialText',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'images',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'urls',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBShareDialogHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'Enum', 'type': 'FBNativeDialogResult', 'converter': 'convert_enum'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBNativeDialogResult, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'canPresentShareDialogWithSession:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBSession',
			'file' : 'FBSession.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'init',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithAppID:permissions:urlSchemeSuffix:tokenCacheStrategy:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'appID',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'urlSchemeSuffix',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSessionTokenCachingStrategy *',
								'name' : 'tokenCachingStrategy',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithAppID:permissions:defaultAudience:urlSchemeSuffix:tokenCacheStrategy:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'appID',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'Enum',
								'type' : 'FBSessionDefaultAudience',
								'name' : 'defaultAudience',
								'converter' : 'convert_enum',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'urlSchemeSuffix',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSessionTokenCachingStrategy *',
								'name' : 'tokenCachingStrategy',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'openWithCompletionHandler:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBSessionStateHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBSession *', 'converter': 'convert_proxy'}, {'kind': 'Enum', 'type': 'FBSessionState', 'converter': 'convert_enum'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBSession *, FBSessionState, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'openWithBehavior:completionHandler:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'Enum',
								'type' : 'FBSessionLoginBehavior',
								'name' : 'behavior',
								'converter' : 'convert_enum',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBSessionStateHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBSession *', 'converter': 'convert_proxy'}, {'kind': 'Enum', 'type': 'FBSessionState', 'converter': 'convert_enum'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBSession *, FBSessionState, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'close',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'closeAndClearTokenInformation',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'reauthorizeWithPermissions:behavior:completionHandler:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'Enum',
								'type' : 'FBSessionLoginBehavior',
								'name' : 'behavior',
								'converter' : 'convert_enum',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBSessionReauthorizeResultHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBSession *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBSession *, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'reauthorizeWithReadPermissions:completionHandler:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'readPermissions',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBSessionReauthorizeResultHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBSession *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBSession *, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'reauthorizeWithPublishPermissions:defaultAudience:completionHandler:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'writePermissions',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'Enum',
								'type' : 'FBSessionDefaultAudience',
								'name' : 'defaultAudience',
								'converter' : 'convert_enum',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBSessionReauthorizeResultHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBSession *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBSession *, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'handleOpenURL:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSURL *',
								'name' : 'url',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'handleDidBecomeActive',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'openActiveSessionWithAllowLoginUI:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'allowLoginUI',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'openActiveSessionWithPermissions:allowLoginUI:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'allowLoginUI',
								'converter' : 'convert_builtin',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBSessionStateHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBSession *', 'converter': 'convert_proxy'}, {'kind': 'Enum', 'type': 'FBSessionState', 'converter': 'convert_enum'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBSession *, FBSessionState, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'openActiveSessionWithReadPermissions:allowLoginUI:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'readPermissions',
								'converter' : 'convert_array',
						},
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'allowLoginUI',
								'converter' : 'convert_builtin',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBSessionStateHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBSession *', 'converter': 'convert_proxy'}, {'kind': 'Enum', 'type': 'FBSessionState', 'converter': 'convert_enum'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBSession *, FBSessionState, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'openActiveSessionWithPublishPermissions:defaultAudience:allowLoginUI:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'publishPermissions',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'Enum',
								'type' : 'FBSessionDefaultAudience',
								'name' : 'defaultAudience',
								'converter' : 'convert_enum',
						},
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'allowLoginUI',
								'converter' : 'convert_builtin',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBSessionStateHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBSession *', 'converter': 'convert_proxy'}, {'kind': 'Enum', 'type': 'FBSessionState', 'converter': 'convert_enum'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBSession *, FBSessionState, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'activeSession',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setActiveSession:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setDefaultAppID:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'appID',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'defaultAppID',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'isOpen',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'state',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Enum',
								'type' : 'FBSessionState',
								'converter' : 'convert_enum',
						},
					],
				},
				{
					'selector' : 'appID',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'urlSchemeSuffix',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'accessToken',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'expirationDate',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDate *',
								'converter' : 'convert_date',
						},
					],
				},
				{
					'selector' : 'permissions',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'converter' : 'convert_array',
						},
					],
				},
				{
					'selector' : 'loginType',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Enum',
								'type' : 'FBSessionLoginType',
								'converter' : 'convert_enum',
						},
					],
				},
				{
					'selector' : 'setLoginType:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'Enum',
								'type' : 'FBSessionLoginType',
								'name' : 'loginType',
								'converter' : 'convert_enum',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'useSafariForLogin',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setUseSafariForLogin:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'useSafariForLogin',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBRequestConnection',
			'file' : 'FBRequestConnection.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'init',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithTimeout:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'NSTimeInterval',
								'kind' : 'Builtin',
								'type' : 'double',
								'name' : 'timeout',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'addRequest:completionHandler:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'name' : 'request',
								'converter' : 'convert_proxy',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'addRequest:completionHandler:batchEntryName:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'name' : 'request',
								'converter' : 'convert_proxy',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'name',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'start',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'cancel',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'startForMeWithCompletionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'startForMyFriendsWithCompletionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'startForUploadPhoto:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIImage *',
								'name' : 'photo',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'startForPostStatusUpdate:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'message',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'startForPostStatusUpdate:place:tags:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'message',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'place',
								'converter' : 'convert_object',
						},
						{
								'conforms_to' : ['NSFastEnumeration'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<NSFastEnumeration>',
								'name' : 'tags',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'startForPlacesSearchAtCoordinate:radiusInMeters:resultsLimit:searchText:completionHandler:',
					'tags' : ['_static', '_no_proxy'],
					'parameters' : [
						{
								'kind' : 'Record',
								'type' : 'CLLocationCoordinate2D',
								'name' : 'coordinate',
								'converter' : '_TODO_',
						},
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'name' : 'radius',
								'converter' : 'convert_builtin',
						},
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'name' : 'limit',
								'converter' : 'convert_builtin',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'searchText',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'startWithGraphPath:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'startForPostWithGraphPath:graphObject:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphObject>',
								'name' : 'graphObject',
								'converter' : 'convert_proxy',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'startWithGraphPath:parameters:HTTPMethod:completionHandler:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDictionary *',
								'name' : 'parameters',
								'converter' : 'convert_dictionary',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'HTTPMethod',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'urlRequest',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSMutableURLRequest *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setUrlRequest:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSMutableURLRequest *',
								'name' : 'urlRequest',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'urlResponse',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSHTTPURLResponse *',
								'converter' : 'convert_object',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBRequest',
			'file' : 'FBRequest.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'init',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithSession:graphPath:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithSession:graphPath:parameters:HTTPMethod:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDictionary *',
								'name' : 'parameters',
								'converter' : 'convert_dictionary',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'HTTPMethod',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initForPostWithSession:graphPath:graphObject:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphObject>',
								'name' : 'graphObject',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithSession:restMethod:parameters:HTTPMethod:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'restMethod',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDictionary *',
								'name' : 'parameters',
								'converter' : 'convert_dictionary',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'HTTPMethod',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'startWithCompletionHandler:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'BlockPointer',
								'declared_type' : 'FBRequestHandler',
								'name' : 'handler',
								'parameters' : [{'kind': 'ObjCObjectPointer', 'type': 'FBRequestConnection *', 'converter': 'convert_proxy'}, {'kind': 'ObjCObjectPointer', 'type': 'id', 'converter': 'convert_object'}, {'kind': 'ObjCObjectPointer', 'type': 'NSError *', 'converter': 'convert_error'}],
								'returns' : [{'kind': 'Builtin', 'type': 'void', 'converter': 'convert_builtin'}],
								'type' : 'void (^)(FBRequestConnection *, id, NSError *)',
								'converter' : 'convert_block',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequestConnection *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestForMe',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestForMyFriends',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestForUploadPhoto:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIImage *',
								'name' : 'photo',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestForPostStatusUpdate:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'message',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestForPostStatusUpdate:place:tags:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'message',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'place',
								'converter' : 'convert_object',
						},
						{
								'conforms_to' : ['NSFastEnumeration'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<NSFastEnumeration>',
								'name' : 'tags',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestForPlacesSearchAtCoordinate:radiusInMeters:resultsLimit:searchText:',
					'tags' : ['_static', '_no_proxy'],
					'parameters' : [
						{
								'kind' : 'Record',
								'type' : 'CLLocationCoordinate2D',
								'name' : 'coordinate',
								'converter' : '_TODO_',
						},
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'name' : 'radius',
								'converter' : 'convert_builtin',
						},
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'name' : 'limit',
								'converter' : 'convert_builtin',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'searchText',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestForGraphPath:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestForPostWithGraphPath:graphObject:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphObject>',
								'name' : 'graphObject',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'requestWithGraphPath:parameters:HTTPMethod:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDictionary *',
								'name' : 'parameters',
								'converter' : 'convert_dictionary',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'HTTPMethod',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBRequest *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'parameters',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSMutableDictionary *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'session',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setSession:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'graphPath',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setGraphPath:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'graphPath',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'restMethod',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setRestMethod:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'restMethod',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'HTTPMethod',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setHTTPMethod:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'HTTPMethod',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'graphObject',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphObject>',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setGraphObject:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphObject>',
								'name' : 'graphObject',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBUserSettingsViewController',
			'file' : 'FBUserSettingsViewController.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'permissions',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'converter' : 'convert_array',
						},
					],
				},
				{
					'selector' : 'setPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'readPermissions',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'converter' : 'convert_array',
						},
					],
				},
				{
					'selector' : 'setReadPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'readPermissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'publishPermissions',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'converter' : 'convert_array',
						},
					],
				},
				{
					'selector' : 'setPublishPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'publishPermissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'defaultAudience',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Enum',
								'type' : 'FBSessionDefaultAudience',
								'converter' : 'convert_enum',
						},
					],
				},
				{
					'selector' : 'setDefaultAudience:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'Enum',
								'type' : 'FBSessionDefaultAudience',
								'name' : 'defaultAudience',
								'converter' : 'convert_enum',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBCacheDescriptor',
			'file' : 'FBCacheDescriptor.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'prefetchAndCacheForSession:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBSettings',
			'file' : 'FBSettings.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'loggingBehavior',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSSet *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setLoggingBehavior:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSSet *',
								'name' : 'loggingBehavior',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'shouldAutoPublishInstall',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setShouldAutoPublishInstall:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'autoPublishInstall',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'publishInstall:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'appID',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBFriendPickerViewController',
			'file' : 'FBFriendPickerViewController.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'init',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithCoder:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSCoder *',
								'name' : 'aDecoder',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithNibName:bundle:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'nibNameOrNil',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSBundle *',
								'name' : 'nibBundleOrNil',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'configureUsingCachedDescriptor:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBCacheDescriptor *',
								'name' : 'cacheDescriptor',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'loadData',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'updateView',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'clearSelection',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'cacheDescriptor',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBCacheDescriptor *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'cacheDescriptorWithUserID:fieldsForRequest:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'userID',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSSet *',
								'name' : 'fieldsForRequest',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBCacheDescriptor *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'spinner',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIActivityIndicatorView *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setSpinner:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIActivityIndicatorView *',
								'name' : 'spinner',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'tableView',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UITableView *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setTableView:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UITableView *',
								'name' : 'tableView',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'allowsMultipleSelection',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setAllowsMultipleSelection:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'allowsMultipleSelection',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'itemPicturesEnabled',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setItemPicturesEnabled:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'itemPicturesEnabled',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'fieldsForRequest',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSSet *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setFieldsForRequest:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSSet *',
								'name' : 'fieldsForRequest',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'session',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setSession:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'userID',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setUserID:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'userID',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'selection',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'converter' : 'convert_array',
						},
					],
				},
				{
					'selector' : 'sortOrdering',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Enum',
								'type' : 'FBFriendSortOrdering',
								'converter' : 'convert_enum',
						},
					],
				},
				{
					'selector' : 'setSortOrdering:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'Enum',
								'type' : 'FBFriendSortOrdering',
								'name' : 'sortOrdering',
								'converter' : 'convert_enum',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'displayOrdering',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Enum',
								'type' : 'FBFriendDisplayOrdering',
								'converter' : 'convert_enum',
						},
					],
				},
				{
					'selector' : 'setDisplayOrdering:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'Enum',
								'type' : 'FBFriendDisplayOrdering',
								'name' : 'displayOrdering',
								'converter' : 'convert_enum',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBLoginView',
			'file' : 'FBLoginView.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'init',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithReadPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'readPermissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithPublishPermissions:defaultAudience:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'publishPermissions',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'Enum',
								'type' : 'FBSessionDefaultAudience',
								'name' : 'defaultAudience',
								'converter' : 'convert_enum',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'permissions',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'converter' : 'convert_array',
						},
					],
				},
				{
					'selector' : 'setPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'readPermissions',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'converter' : 'convert_array',
						},
					],
				},
				{
					'selector' : 'setReadPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'readPermissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'publishPermissions',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'converter' : 'convert_array',
						},
					],
				},
				{
					'selector' : 'setPublishPermissions:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'publishPermissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'defaultAudience',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Enum',
								'type' : 'FBSessionDefaultAudience',
								'converter' : 'convert_enum',
						},
					],
				},
				{
					'selector' : 'setDefaultAudience:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'Enum',
								'type' : 'FBSessionDefaultAudience',
								'name' : 'defaultAudience',
								'converter' : 'convert_enum',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'delegate',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'conforms_to' : ['FBLoginViewDelegate'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBLoginViewDelegate>',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setDelegate:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'conforms_to' : ['FBLoginViewDelegate'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBLoginViewDelegate>',
								'name' : 'delegate',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBGraphObject',
			'file' : 'FBGraphObject.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'graphObject',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSMutableDictionary<FBGraphObject> *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'graphObjectWrappingDictionary:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSDictionary *',
								'name' : 'jsonDictionary',
								'converter' : 'convert_dictionary',
						},
					],
					'returns' : [
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSMutableDictionary<FBGraphObject> *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'isGraphObjectID:sameAs:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphObject>',
								'name' : 'anObject',
								'converter' : 'convert_proxy',
						},
						{
								'conforms_to' : ['FBGraphObject'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphObject>',
								'name' : 'anotherObject',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'count',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'NSUInteger',
								'kind' : 'Builtin',
								'type' : 'unsigned int',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'objectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'keyEnumerator',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSEnumerator *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'removeObjectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setObject:forKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'anObject',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBTestSession',
			'file' : 'FBTestSession.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'sessionWithSharedUserWithPermissions:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'sessionWithSharedUserWithPermissions:uniqueUserTag:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'uniqueUserTag',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'sessionWithPrivateUserWithPermissions:',
					'tags' : ['_static', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSArray *',
								'name' : 'permissions',
								'converter' : 'convert_array',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'appAccessToken',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'testUserID',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'testAppID',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'testAppSecret',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBPlacePickerViewController',
			'file' : 'FBPlacePickerViewController.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'clearSelection',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'init',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithCoder:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSCoder *',
								'name' : 'aDecoder',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'initWithNibName:bundle:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'nibNameOrNil',
								'converter' : 'convert_string',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSBundle *',
								'name' : 'nibBundleOrNil',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'configureUsingCachedDescriptor:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBCacheDescriptor *',
								'name' : 'cacheDescriptor',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'loadData',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'cacheDescriptorWithLocationCoordinate:radiusInMeters:searchText:resultsLimit:fieldsForRequest:',
					'tags' : ['_static', '_no_proxy'],
					'parameters' : [
						{
								'kind' : 'Record',
								'type' : 'CLLocationCoordinate2D',
								'name' : 'locationCoordinate',
								'converter' : '_TODO_',
						},
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'name' : 'radiusInMeters',
								'converter' : 'convert_builtin',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'searchText',
								'converter' : 'convert_string',
						},
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'name' : 'resultsLimit',
								'converter' : 'convert_builtin',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSSet *',
								'name' : 'fieldsForRequest',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBCacheDescriptor *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'spinner',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIActivityIndicatorView *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setSpinner:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UIActivityIndicatorView *',
								'name' : 'spinner',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'tableView',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UITableView *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setTableView:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'UITableView *',
								'name' : 'tableView',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'fieldsForRequest',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSSet *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setFieldsForRequest:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSSet *',
								'name' : 'fieldsForRequest',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'itemPicturesEnabled',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setItemPicturesEnabled:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'BOOL',
								'kind' : 'Builtin',
								'type' : 'signed char',
								'name' : 'itemPicturesEnabled',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'locationCoordinate',
					'tags' : ['_instance', '_no_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'Record',
								'type' : 'CLLocationCoordinate2D',
								'converter' : '_TODO_',
						},
					],
				},
				{
					'selector' : 'setLocationCoordinate:',
					'tags' : ['_instance', '_no_proxy'],
					'parameters' : [
						{
								'kind' : 'Record',
								'type' : 'CLLocationCoordinate2D',
								'name' : 'locationCoordinate',
								'converter' : '_TODO_',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'radiusInMeters',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setRadiusInMeters:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'name' : 'radiusInMeters',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'resultsLimit',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setResultsLimit:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'declared_type' : 'NSInteger',
								'kind' : 'Builtin',
								'type' : 'int',
								'name' : 'resultsLimit',
								'converter' : 'convert_builtin',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'searchText',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setSearchText:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'searchText',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'session',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setSession:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBSession *',
								'name' : 'session',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'selection',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'conforms_to' : ['FBGraphPlace'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphPlace>',
								'converter' : 'convert_proxy',
						},
					],
				},
			],	
		},
	],
	'protocols' : [
		{
			'name' : 'FBViewControllerDelegate',
			'file' : 'FBViewController.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'facebookViewControllerCancelWasPressed:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'sender',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'facebookViewControllerDoneWasPressed:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'sender',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBGraphObject',
			'file' : 'FBGraphObject.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'count',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'NSUInteger',
								'kind' : 'Builtin',
								'type' : 'unsigned int',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'objectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'keyEnumerator',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSEnumerator *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'removeObjectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setObject:forKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'anObject',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBLoginViewDelegate',
			'file' : 'FBLoginView.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'loginViewShowingLoggedInUser:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBLoginView *',
								'name' : 'loginView',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'loginViewFetchedUserInfo:user:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBLoginView *',
								'name' : 'loginView',
								'converter' : 'convert_proxy',
						},
						{
								'conforms_to' : ['FBGraphUser'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphUser>',
								'name' : 'user',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'loginViewShowingLoggedOutUser:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'FBLoginView *',
								'name' : 'loginView',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBGraphUser',
			'file' : 'FBGraphUser.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'id',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setId:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'id',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'name',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setName:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'name',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'first_name',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setFirst_name:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'first_name',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'middle_name',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setMiddle_name:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'middle_name',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'last_name',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setLast_name:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'last_name',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'link',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setLink:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'link',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'username',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setUsername:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'username',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'birthday',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setBirthday:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'birthday',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'location',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'conforms_to' : ['FBGraphPlace'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphPlace>',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setLocation:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'conforms_to' : ['FBGraphPlace'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphPlace>',
								'name' : 'location',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'count',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'NSUInteger',
								'kind' : 'Builtin',
								'type' : 'unsigned int',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'objectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'keyEnumerator',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSEnumerator *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'removeObjectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setObject:forKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'anObject',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBGraphPlace',
			'file' : 'FBGraphPlace.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'id',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setId:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'id',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'name',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setName:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'name',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'category',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setCategory:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'category',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'location',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'conforms_to' : ['FBGraphLocation'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphLocation>',
								'converter' : 'convert_proxy',
						},
					],
				},
				{
					'selector' : 'setLocation:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'conforms_to' : ['FBGraphLocation'],
								'kind' : 'ObjCObjectPointer',
								'type' : 'id<FBGraphLocation>',
								'name' : 'location',
								'converter' : 'convert_proxy',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'count',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'NSUInteger',
								'kind' : 'Builtin',
								'type' : 'unsigned int',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'objectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'keyEnumerator',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSEnumerator *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'removeObjectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setObject:forKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'anObject',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
		{
			'name' : 'FBGraphLocation',
			'file' : 'FBGraphLocation.h',
			'tags' : ['_proxy'],
			'methods' : [
				{
					'selector' : 'street',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setStreet:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'street',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'city',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setCity:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'city',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'state',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setState:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'state',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'country',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setCountry:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'country',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'zip',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'converter' : 'convert_string',
						},
					],
				},
				{
					'selector' : 'setZip:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSString *',
								'name' : 'zip',
								'converter' : 'convert_string',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'latitude',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSNumber *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setLatitude:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSNumber *',
								'name' : 'latitude',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'longitude',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSNumber *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'setLongitude:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSNumber *',
								'name' : 'longitude',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'count',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'declared_type' : 'NSUInteger',
								'kind' : 'Builtin',
								'type' : 'unsigned int',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'objectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'keyEnumerator',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
					],
					'returns' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'NSEnumerator *',
								'converter' : 'convert_object',
						},
					],
				},
				{
					'selector' : 'removeObjectForKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
				{
					'selector' : 'setObject:forKey:',
					'tags' : ['_instance', '_proxy'],
					'parameters' : [
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'anObject',
								'converter' : 'convert_object',
						},
						{
								'kind' : 'ObjCObjectPointer',
								'type' : 'id',
								'name' : 'aKey',
								'converter' : 'convert_object',
						},
					],
					'returns' : [
						{
								'kind' : 'Builtin',
								'type' : 'void',
								'converter' : 'convert_builtin',
						},
					],
				},
			],	
		},
	],
}