# AdvisoryGHSAEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed** | **str** |  | [optional] 
**introduced** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ghsa_event import AdvisoryGHSAEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHSAEvent from a JSON string
advisory_ghsa_event_instance = AdvisoryGHSAEvent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHSAEvent.to_json())

# convert the object into a dict
advisory_ghsa_event_dict = advisory_ghsa_event_instance.to_dict()
# create an instance of AdvisoryGHSAEvent from a dict
advisory_ghsa_event_from_dict = AdvisoryGHSAEvent.from_dict(advisory_ghsa_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


