# ReturnIntegrationRequest

The body of a return integration API request. Next to the cart items details, this contains an optional listing of extra properties that should be returned in the response.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_return** | [**NewReturn**](NewReturn.md) |  | 
**response_content** | **list[str]** | Optional list of extra data that you want to get in the response. Use this property to get as much data as you need in one request instead of sending extra requests to other endpoints.  **Note:** &#x60;ruleFailureReasons&#x60; is always part of the response when the [Application type](https://docs.talon.one/docs/product/applications/overview#application-types) is &#x60;sandbox&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

