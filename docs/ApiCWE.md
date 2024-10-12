# ApiCWE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abstraction** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**kev_count** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**structure** | **str** |  | [optional] 
**vulncheck_nvd_count** | **int** |  | [optional] 
**weakness_id** | **str** |  | [optional] 
**weakness_name** | **str** |  | [optional] 
**weighted_score** | **float** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cwe import ApiCWE

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCWE from a JSON string
api_cwe_instance = ApiCWE.from_json(json)
# print the JSON string representation of the object
print(ApiCWE.to_json())

# convert the object into a dict
api_cwe_dict = api_cwe_instance.to_dict()
# create an instance of ApiCWE from a dict
api_cwe_from_dict = ApiCWE.from_dict(api_cwe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


