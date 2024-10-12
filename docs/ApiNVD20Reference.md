# ApiNVD20Reference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_reference import ApiNVD20Reference

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20Reference from a JSON string
api_nvd20_reference_instance = ApiNVD20Reference.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20Reference.to_json())

# convert the object into a dict
api_nvd20_reference_dict = api_nvd20_reference_instance.to_dict()
# create an instance of ApiNVD20Reference from a dict
api_nvd20_reference_from_dict = ApiNVD20Reference.from_dict(api_nvd20_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


