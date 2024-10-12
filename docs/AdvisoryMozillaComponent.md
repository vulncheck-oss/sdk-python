# AdvisoryMozillaComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bugzilla** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**reporter** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mozilla_component import AdvisoryMozillaComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMozillaComponent from a JSON string
advisory_mozilla_component_instance = AdvisoryMozillaComponent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMozillaComponent.to_json())

# convert the object into a dict
advisory_mozilla_component_dict = advisory_mozilla_component_instance.to_dict()
# create an instance of AdvisoryMozillaComponent from a dict
advisory_mozilla_component_from_dict = AdvisoryMozillaComponent.from_dict(advisory_mozilla_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


