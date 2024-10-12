# AdvisoryEcoSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** |  | [optional] 
**spl** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_eco_system import AdvisoryEcoSystem

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEcoSystem from a JSON string
advisory_eco_system_instance = AdvisoryEcoSystem.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEcoSystem.to_json())

# convert the object into a dict
advisory_eco_system_dict = advisory_eco_system_instance.to_dict()
# create an instance of AdvisoryEcoSystem from a dict
advisory_eco_system_from_dict = AdvisoryEcoSystem.from_dict(advisory_eco_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


