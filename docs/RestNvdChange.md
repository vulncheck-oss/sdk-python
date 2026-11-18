# RestNvdChange

rest.NvdChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** |  | [optional] 
**cve_change_id** | **str** |  | [optional] 
**cve_id** | **str** |  | [optional] 
**details** | [**List[RestNvdChangeDetail]**](RestNvdChangeDetail.md) |  | [optional] 
**event_name** | **str** |  | [optional] 
**source_identifier** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.rest_nvd_change import RestNvdChange

# TODO update the JSON string below
json = "{}"
# create an instance of RestNvdChange from a JSON string
rest_nvd_change_instance = RestNvdChange.from_json(json)
# print the JSON string representation of the object
print(RestNvdChange.to_json())

# convert the object into a dict
rest_nvd_change_dict = rest_nvd_change_instance.to_dict()
# create an instance of RestNvdChange from a dict
rest_nvd_change_from_dict = RestNvdChange.from_dict(rest_nvd_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


