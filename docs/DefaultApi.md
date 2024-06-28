# swagger_client.DefaultApi

All URIs are relative to *https://umsxtend.blinkx.in/auth/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_normal_login_post**](DefaultApi.md#login_normal_login_post) | **POST** /login/normal-login | User login

# **login_normal_login_post**
> InlineResponse200 login_normal_login_post(body, app_id)

User login

Endpoint for normal user login

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.LoginNormalloginBody() # LoginNormalloginBody | 
app_id = 'app_id_example' # str | Application ID

try:
    # User login
    api_response = api_instance.login_normal_login_post(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->login_normal_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginNormalloginBody**](LoginNormalloginBody.md)|  | 
 **app_id** | **str**| Application ID | 

### Return type

[**InlineResponse200**](LoginResponse)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

