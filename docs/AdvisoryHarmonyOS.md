# AdvisoryHarmonyOS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_harmony_os import AdvisoryHarmonyOS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHarmonyOS from a JSON string
advisory_harmony_os_instance = AdvisoryHarmonyOS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHarmonyOS.to_json())

# convert the object into a dict
advisory_harmony_os_dict = advisory_harmony_os_instance.to_dict()
# create an instance of AdvisoryHarmonyOS from a dict
advisory_harmony_os_from_dict = AdvisoryHarmonyOS.from_dict(advisory_harmony_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


