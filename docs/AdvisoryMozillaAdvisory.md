# AdvisoryMozillaAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_components** | [**List[AdvisoryMozillaComponent]**](AdvisoryMozillaComponent.md) |  | [optional] 
**bugzilla** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fixed_in** | **List[str]** |  | [optional] 
**impact** | **str** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**reporter** | **str** |  | [optional] 
**risk** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mozilla_advisory import AdvisoryMozillaAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMozillaAdvisory from a JSON string
advisory_mozilla_advisory_instance = AdvisoryMozillaAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMozillaAdvisory.to_json())

# convert the object into a dict
advisory_mozilla_advisory_dict = advisory_mozilla_advisory_instance.to_dict()
# create an instance of AdvisoryMozillaAdvisory from a dict
advisory_mozilla_advisory_from_dict = AdvisoryMozillaAdvisory.from_dict(advisory_mozilla_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


