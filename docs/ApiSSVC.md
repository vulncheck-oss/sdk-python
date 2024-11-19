# ApiSSVC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatable** | **str** |  | [optional] 
**exploitation** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**technical_impact** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_ssvc import ApiSSVC

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSSVC from a JSON string
api_ssvc_instance = ApiSSVC.from_json(json)
# print the JSON string representation of the object
print(ApiSSVC.to_json())

# convert the object into a dict
api_ssvc_dict = api_ssvc_instance.to_dict()
# create an instance of ApiSSVC from a dict
api_ssvc_from_dict = ApiSSVC.from_dict(api_ssvc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


