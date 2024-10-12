# AdvisoryUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** | sort // key | [optional] 
**issued** | [**AdvisoryDateTime**](AdvisoryDateTime.md) |  | [optional] 
**os_arch** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**packages** | [**List[AdvisoryPackage]**](AdvisoryPackage.md) |  | [optional] 
**references** | [**List[AdvisoryReference]**](AdvisoryReference.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated** | [**AdvisoryDateTime**](AdvisoryDateTime.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_update import AdvisoryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryUpdate from a JSON string
advisory_update_instance = AdvisoryUpdate.from_json(json)
# print the JSON string representation of the object
print(AdvisoryUpdate.to_json())

# convert the object into a dict
advisory_update_dict = advisory_update_instance.to_dict()
# create an instance of AdvisoryUpdate from a dict
advisory_update_from_dict = AdvisoryUpdate.from_dict(advisory_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


