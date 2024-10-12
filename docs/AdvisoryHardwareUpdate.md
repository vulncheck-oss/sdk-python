# AdvisoryHardwareUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_versions** | **str** |  | [optional] 
**cves** | **List[str]** |  | [optional] 
**hardware_platform** | **str** |  | [optional] 
**system** | **str** |  | [optional] 
**updated_version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hardware_update import AdvisoryHardwareUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHardwareUpdate from a JSON string
advisory_hardware_update_instance = AdvisoryHardwareUpdate.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHardwareUpdate.to_json())

# convert the object into a dict
advisory_hardware_update_dict = advisory_hardware_update_instance.to_dict()
# create an instance of AdvisoryHardwareUpdate from a dict
advisory_hardware_update_from_dict = AdvisoryHardwareUpdate.from_dict(advisory_hardware_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


