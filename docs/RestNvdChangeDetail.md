# RestNvdChangeDetail

rest.NvdChangeDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**new_value** | **object** | A string, an array or an object, depending on the change type. | [optional] 
**old_value** | **object** | A string, an array or an object, depending on the change type. | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.rest_nvd_change_detail import RestNvdChangeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RestNvdChangeDetail from a JSON string
rest_nvd_change_detail_instance = RestNvdChangeDetail.from_json(json)
# print the JSON string representation of the object
print(RestNvdChangeDetail.to_json())

# convert the object into a dict
rest_nvd_change_detail_dict = rest_nvd_change_detail_instance.to_dict()
# create an instance of RestNvdChangeDetail from a dict
rest_nvd_change_detail_from_dict = RestNvdChangeDetail.from_dict(rest_nvd_change_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


