# ApiCPEMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe22_uri** | **str** |  | [optional] 
**cpe23_uri** | **str** |  | [optional] 
**cpe_name** | [**List[ApiCPEName]**](ApiCPEName.md) |  | [optional] 
**version_end_excluding** | **str** |  | [optional] 
**version_end_including** | **str** |  | [optional] 
**version_start_excluding** | **str** |  | [optional] 
**version_start_including** | **str** |  | [optional] 
**vulnerable** | **bool** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cpe_match import ApiCPEMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCPEMatch from a JSON string
api_cpe_match_instance = ApiCPEMatch.from_json(json)
# print the JSON string representation of the object
print(ApiCPEMatch.to_json())

# convert the object into a dict
api_cpe_match_dict = api_cpe_match_instance.to_dict()
# create an instance of ApiCPEMatch from a dict
api_cpe_match_from_dict = ApiCPEMatch.from_dict(api_cpe_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


