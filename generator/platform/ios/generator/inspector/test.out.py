{'enums': [{'constants': [{'name': 'FBSessionDefaultAudienceNone',
                           'value': '0'},
                          {'name': 'FBSessionDefaultAudienceOnlyMe',
                           'value': '10'},
                          {'name': 'FBSessionDefaultAudienceFriends',
                           'value': '20'},
                          {'name': 'FBSessionDefaultAudienceEveryone',
                           'value': '30'}],
            'typedef': 'FBSessionDefaultAudience'},
           {'constants': [{'name': 'FBSessionStateCreated', 'value': '0'},
                          {'name': 'FBSessionStateCreatedTokenLoaded',
                           'value': '1'},
                          {'name': 'FBSessionStateCreatedOpening',
                           'value': '2'},
                          {'name': 'FBSessionStateOpen', 'value': '513'},
                          {'name': 'FBSessionStateOpenTokenExtended',
                           'value': '514'},
                          {'name': 'FBSessionStateClosedLoginFailed',
                           'value': '257'},
                          {'name': 'FBSessionStateClosed', 'value': '258'}],
            'typedef': 'FBSessionState'},
           {'constants': [{'name': 'FBSessionLoginBehaviorWithFallbackToWebView',
                           'value': '0'},
                          {'name': 'FBSessionLoginBehaviorWithNoFallbackToWebView',
                           'value': '1'},
                          {'name': 'FBSessionLoginBehaviorForcingWebView',
                           'value': '2'},
                          {'name': 'FBSessionLoginBehaviorUseSystemAccountIfPresent',
                           'value': '3'}],
            'typedef': 'FBSessionLoginBehavior'},
           {'constants': [{'name': 'FBSessionLoginTypeNone', 'value': '0'},
                          {'name': 'FBSessionLoginTypeSystemAccount',
                           'value': '1'},
                          {'name': 'FBSessionLoginTypeFacebookApplication',
                           'value': '2'},
                          {'name': 'FBSessionLoginTypeFacebookViaSafari',
                           'value': '3'},
                          {'name': 'FBSessionLoginTypeWebView',
                           'value': '4'},
                          {'name': 'FBSessionLoginTypeTestUser',
                           'value': '5'}],
            'typedef': 'FBSessionLoginType'}],
 'frameworks': ['/Users/wsouza/projects/ZDK/cxx-bindings-generator/ios/samples/facebook-ios-sdk/build/FacebookSDK.framework'],
 'interfaces': [{'methods': [{'name': 'init',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'initWithPermissions',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'permissions',
                                              'type': 'NSArray *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'initWithAppID_permissions_urlSchemeSuffix_tokenCacheStrategy',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'appID',
                                              'type': 'NSString *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'permissions',
                                              'type': 'NSArray *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'urlSchemeSuffix',
                                              'type': 'NSString *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'tokenCachingStrategy',
                                              'type': 'FBSessionTokenCachingStrategy *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'initWithAppID_permissions_defaultAudience_urlSchemeSuffix_tokenCacheStrategy',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'appID',
                                              'type': 'NSString *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'permissions',
                                              'type': 'NSArray *'},
                                             {'kind': 'Enum',
                                              'name': 'defaultAudience',
                                              'type': 'FBSessionDefaultAudience'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'urlSchemeSuffix',
                                              'type': 'NSString *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'tokenCachingStrategy',
                                              'type': 'FBSessionTokenCachingStrategy *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'openWithCompletionHandler',
                              'parameters': [{'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBSession *'},
                                                             {'kind': 'Enum',
                                                              'type': 'FBSessionState'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBSession *, FBSessionState, NSError *)'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'openWithBehavior_completionHandler',
                              'parameters': [{'kind': 'Enum',
                                              'name': 'behavior',
                                              'type': 'FBSessionLoginBehavior'},
                                             {'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBSession *'},
                                                             {'kind': 'Enum',
                                                              'type': 'FBSessionState'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBSession *, FBSessionState, NSError *)'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'close',
                              'parameters': [],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'closeAndClearTokenInformation',
                              'parameters': [],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'reauthorizeWithPermissions_behavior_completionHandler',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'permissions',
                                              'type': 'NSArray *'},
                                             {'kind': 'Enum',
                                              'name': 'behavior',
                                              'type': 'FBSessionLoginBehavior'},
                                             {'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBSession *'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBSession *, NSError *)'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'reauthorizeWithReadPermissions_completionHandler',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'readPermissions',
                                              'type': 'NSArray *'},
                                             {'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBSession *'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBSession *, NSError *)'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'reauthorizeWithPublishPermissions_defaultAudience_completionHandler',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'writePermissions',
                                              'type': 'NSArray *'},
                                             {'kind': 'Enum',
                                              'name': 'defaultAudience',
                                              'type': 'FBSessionDefaultAudience'},
                                             {'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBSession *'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBSession *, NSError *)'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'handleOpenURL',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'url',
                                              'type': 'NSURL *'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'signed char'}]},
                             {'name': 'handleDidBecomeActive',
                              'parameters': [],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'openActiveSessionWithAllowLoginUI',
                              'parameters': [{'kind': 'Builtin',
                                              'name': 'allowLoginUI',
                                              'type': 'signed char'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'signed char'}],
                              'tags': ['_static']},
                             {'name': 'openActiveSessionWithPermissions_allowLoginUI_completionHandler',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'permissions',
                                              'type': 'NSArray *'},
                                             {'kind': 'Builtin',
                                              'name': 'allowLoginUI',
                                              'type': 'signed char'},
                                             {'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBSession *'},
                                                             {'kind': 'Enum',
                                                              'type': 'FBSessionState'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBSession *, FBSessionState, NSError *)'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'signed char'}],
                              'tags': ['_static']},
                             {'name': 'openActiveSessionWithReadPermissions_allowLoginUI_completionHandler',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'readPermissions',
                                              'type': 'NSArray *'},
                                             {'kind': 'Builtin',
                                              'name': 'allowLoginUI',
                                              'type': 'signed char'},
                                             {'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBSession *'},
                                                             {'kind': 'Enum',
                                                              'type': 'FBSessionState'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBSession *, FBSessionState, NSError *)'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'signed char'}],
                              'tags': ['_static']},
                             {'name': 'openActiveSessionWithPublishPermissions_defaultAudience_allowLoginUI_completionHandler',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'publishPermissions',
                                              'type': 'NSArray *'},
                                             {'kind': 'Enum',
                                              'name': 'defaultAudience',
                                              'type': 'FBSessionDefaultAudience'},
                                             {'kind': 'Builtin',
                                              'name': 'allowLoginUI',
                                              'type': 'signed char'},
                                             {'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBSession *'},
                                                             {'kind': 'Enum',
                                                              'type': 'FBSessionState'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBSession *, FBSessionState, NSError *)'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'signed char'}],
                              'tags': ['_static']},
                             {'name': 'activeSession',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBSession *'}],
                              'tags': ['_static']},
                             {'name': 'setActiveSession',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'session',
                                              'type': 'FBSession *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBSession *'}],
                              'tags': ['_static']},
                             {'name': 'setDefaultAppID',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'appID',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}],
                              'tags': ['_static']},
                             {'name': 'defaultAppID',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSString *'}],
                              'tags': ['_static']},
                             {'name': 'isOpen',
                              'parameters': [],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'signed char'}]},
                             {'name': 'state',
                              'parameters': [],
                              'returns': [{'kind': 'Enum',
                                           'type': 'FBSessionState'}]},
                             {'name': 'appID',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSString *'}]},
                             {'name': 'urlSchemeSuffix',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSString *'}]},
                             {'name': 'accessToken',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSString *'}]},
                             {'name': 'expirationDate',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSDate *'}]},
                             {'name': 'permissions',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSArray *'}]},
                             {'name': 'loginType',
                              'parameters': [],
                              'returns': [{'kind': 'Enum',
                                           'type': 'FBSessionLoginType'}]},
                             {'name': 'setLoginType',
                              'parameters': [{'kind': 'Enum',
                                              'name': 'loginType',
                                              'type': 'FBSessionLoginType'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'useSafariForLogin',
                              'parameters': [],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'signed char'}]},
                             {'name': 'setUseSafariForLogin',
                              'parameters': [{'kind': 'Builtin',
                                              'name': 'useSafariForLogin',
                                              'type': 'signed char'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]}],
                 'name': 'FBSession'},
                {'methods': [{'name': 'init',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'initWithSession_graphPath',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'session',
                                              'type': 'FBSession *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'graphPath',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'initWithSession_graphPath_parameters_HTTPMethod',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'session',
                                              'type': 'FBSession *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'graphPath',
                                              'type': 'NSString *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'parameters',
                                              'type': 'NSDictionary *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'HTTPMethod',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'initForPostWithSession_graphPath_graphObject',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'session',
                                              'type': 'FBSession *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'graphPath',
                                              'type': 'NSString *'},
                                             {'conforms_to': ['FBGraphObject'],
                                              'kind': 'ObjCObjectPointer',
                                              'name': 'graphObject',
                                              'type': 'id<FBGraphObject>'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'initWithSession_restMethod_parameters_HTTPMethod',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'session',
                                              'type': 'FBSession *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'restMethod',
                                              'type': 'NSString *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'parameters',
                                              'type': 'NSDictionary *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'HTTPMethod',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'id'}]},
                             {'name': 'startWithCompletionHandler',
                              'parameters': [{'kind': 'BlockPointer',
                                              'name': 'handler',
                                              'parameters': [{'kind': 'ObjCObjectPointer',
                                                              'type': 'FBRequestConnection *'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'id'},
                                                             {'kind': 'ObjCObjectPointer',
                                                              'type': 'NSError *'}],
                                              'returns': [{'kind': 'Builtin',
                                                           'type': 'void'}],
                                              'type': 'void (^)(FBRequestConnection *, id, NSError *)'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequestConnection *'}]},
                             {'name': 'requestForMe',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'requestForMyFriends',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'requestForUploadPhoto',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'photo',
                                              'type': 'UIImage *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'requestForPostStatusUpdate',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'message',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'requestForPostStatusUpdate_place_tags',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'message',
                                              'type': 'NSString *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'place',
                                              'type': 'id'},
                                             {'conforms_to': ['NSFastEnumeration'],
                                              'kind': 'ObjCObjectPointer',
                                              'name': 'tags',
                                              'type': 'id<NSFastEnumeration>'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'requestForPlacesSearchAtCoordinate_radiusInMeters_resultsLimit_searchText',
                              'parameters': [{'kind': 'Record',
                                              'name': 'coordinate',
                                              'type': 'CLLocationCoordinate2D'},
                                             {'kind': 'Builtin',
                                              'name': 'radius',
                                              'type': 'int'},
                                             {'kind': 'Builtin',
                                              'name': 'limit',
                                              'type': 'int'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'searchText',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'requestForGraphPath',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'graphPath',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'requestForPostWithGraphPath_graphObject',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'graphPath',
                                              'type': 'NSString *'},
                                             {'conforms_to': ['FBGraphObject'],
                                              'kind': 'ObjCObjectPointer',
                                              'name': 'graphObject',
                                              'type': 'id<FBGraphObject>'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'requestWithGraphPath_parameters_HTTPMethod',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'graphPath',
                                              'type': 'NSString *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'parameters',
                                              'type': 'NSDictionary *'},
                                             {'kind': 'ObjCObjectPointer',
                                              'name': 'HTTPMethod',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBRequest *'}],
                              'tags': ['_static']},
                             {'name': 'parameters',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSMutableDictionary *'}]},
                             {'name': 'session',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'FBSession *'}]},
                             {'name': 'setSession',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'session',
                                              'type': 'FBSession *'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'graphPath',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSString *'}]},
                             {'name': 'setGraphPath',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'graphPath',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'restMethod',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSString *'}]},
                             {'name': 'setRestMethod',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'restMethod',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'HTTPMethod',
                              'parameters': [],
                              'returns': [{'kind': 'ObjCObjectPointer',
                                           'type': 'NSString *'}]},
                             {'name': 'setHTTPMethod',
                              'parameters': [{'kind': 'ObjCObjectPointer',
                                              'name': 'HTTPMethod',
                                              'type': 'NSString *'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]},
                             {'name': 'graphObject',
                              'parameters': [],
                              'returns': [{'conforms_to': ['FBGraphObject'],
                                           'kind': 'ObjCObjectPointer',
                                           'type': 'id<FBGraphObject>'}]},
                             {'name': 'setGraphObject',
                              'parameters': [{'conforms_to': ['FBGraphObject'],
                                              'kind': 'ObjCObjectPointer',
                                              'name': 'graphObject',
                                              'type': 'id<FBGraphObject>'}],
                              'returns': [{'kind': 'Builtin',
                                           'type': 'void'}]}],
                 'name': 'FBRequest'}],
 'protocols': [{'methods': [{'name': 'count',
                             'parameters': [],
                             'returns': [{'kind': 'Builtin',
                                          'type': 'unsigned int'}]},
                            {'name': 'objectForKey',
                             'parameters': [{'kind': 'ObjCObjectPointer',
                                             'name': 'aKey',
                                             'type': 'id'}],
                             'returns': [{'kind': 'ObjCObjectPointer',
                                          'type': 'id'}]},
                            {'name': 'keyEnumerator',
                             'parameters': [],
                             'returns': [{'kind': 'ObjCObjectPointer',
                                          'type': 'NSEnumerator *'}]},
                            {'name': 'removeObjectForKey',
                             'parameters': [{'kind': 'ObjCObjectPointer',
                                             'name': 'aKey',
                                             'type': 'id'}],
                             'returns': [{'kind': 'Builtin',
                                          'type': 'void'}]},
                            {'name': 'setObject_forKey',
                             'parameters': [{'kind': 'ObjCObjectPointer',
                                             'name': 'anObject',
                                             'type': 'id'},
                                            {'kind': 'ObjCObjectPointer',
                                             'name': 'aKey',
                                             'type': 'id'}],
                             'returns': [{'kind': 'Builtin',
                                          'type': 'void'}]}],
                'name': 'FBGraphObject'}]}
