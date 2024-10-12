# AdvisoryThreat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_threat import AdvisoryThreat

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryThreat from a JSON string
advisory_threat_instance = AdvisoryThreat.from_json(json)
# print the JSON string representation of the object
print(AdvisoryThreat.to_json())

# convert the object into a dict
advisory_threat_dict = advisory_threat_instance.to_dict()
# create an instance of AdvisoryThreat from a dict
advisory_threat_from_dict = AdvisoryThreat.from_dict(advisory_threat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


