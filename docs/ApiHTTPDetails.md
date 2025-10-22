# ApiHTTPDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_request_body** | **str** |  | [optional] 
**http_user_agent** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_http_details import ApiHTTPDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHTTPDetails from a JSON string
api_http_details_instance = ApiHTTPDetails.from_json(json)
# print the JSON string representation of the object
print(ApiHTTPDetails.to_json())

# convert the object into a dict
api_http_details_dict = api_http_details_instance.to_dict()
# create an instance of ApiHTTPDetails from a dict
api_http_details_from_dict = ApiHTTPDetails.from_dict(api_http_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


