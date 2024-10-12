# ApiNVD20CPEMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_last_modified** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**criteria** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**match_criteria_id** | **str** |  | [optional] 
**matches** | [**List[ApiNVD20CPEName]**](ApiNVD20CPEName.md) |  | [optional] 
**status** | **str** |  | [optional] 
**version_end_excluding** | **str** |  | [optional] 
**version_end_including** | **str** |  | [optional] 
**version_start_excluding** | **str** |  | [optional] 
**version_start_including** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cpe_match import ApiNVD20CPEMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CPEMatch from a JSON string
api_nvd20_cpe_match_instance = ApiNVD20CPEMatch.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CPEMatch.to_json())

# convert the object into a dict
api_nvd20_cpe_match_dict = api_nvd20_cpe_match_instance.to_dict()
# create an instance of ApiNVD20CPEMatch from a dict
api_nvd20_cpe_match_from_dict = ApiNVD20CPEMatch.from_dict(api_nvd20_cpe_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


