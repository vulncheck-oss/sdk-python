# AdvisoryContainerOS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updates** | [**List[AdvisoryCOSUpdate]**](AdvisoryCOSUpdate.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_container_os import AdvisoryContainerOS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryContainerOS from a JSON string
advisory_container_os_instance = AdvisoryContainerOS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryContainerOS.to_json())

# convert the object into a dict
advisory_container_os_dict = advisory_container_os_instance.to_dict()
# create an instance of AdvisoryContainerOS from a dict
advisory_container_os_from_dict = AdvisoryContainerOS.from_dict(advisory_container_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


