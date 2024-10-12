# AdvisoryAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_specific** | **object** | The meaning of the values within the object is entirely defined by the database | [optional] 
**ecosystem_specific** | **object** | The meaning of the values within the object is entirely defined by the ecosystem | [optional] 
**package** | [**AdvisoryOSVPackage**](AdvisoryOSVPackage.md) |  | [optional] 
**ranges** | [**List[AdvisoryRange]**](AdvisoryRange.md) |  | [optional] 
**severity** | [**List[AdvisorySeverity]**](AdvisorySeverity.md) |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected import AdvisoryAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffected from a JSON string
advisory_affected_instance = AdvisoryAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffected.to_json())

# convert the object into a dict
advisory_affected_dict = advisory_affected_instance.to_dict()
# create an instance of AdvisoryAffected from a dict
advisory_affected_from_dict = AdvisoryAffected.from_dict(advisory_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


