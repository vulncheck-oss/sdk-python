# AdvisoryCOSUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **List[str]** |  | [optional] 
**featured** | **List[str]** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**security** | **List[str]** |  | [optional] 
**updated** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cos_update import AdvisoryCOSUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCOSUpdate from a JSON string
advisory_cos_update_instance = AdvisoryCOSUpdate.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCOSUpdate.to_json())

# convert the object into a dict
advisory_cos_update_dict = advisory_cos_update_instance.to_dict()
# create an instance of AdvisoryCOSUpdate from a dict
advisory_cos_update_from_dict = AdvisoryCOSUpdate.from_dict(advisory_cos_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


