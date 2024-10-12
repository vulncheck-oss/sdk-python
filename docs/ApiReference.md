# ApiReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | sort | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_reference import ApiReference

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReference from a JSON string
api_reference_instance = ApiReference.from_json(json)
# print the JSON string representation of the object
print(ApiReference.to_json())

# convert the object into a dict
api_reference_dict = api_reference_instance.to_dict()
# create an instance of ApiReference from a dict
api_reference_from_dict = ApiReference.from_dict(api_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


