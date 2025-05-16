# AdvisoryGoEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed** | **str** |  | [optional] 
**introduced** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_go_event import AdvisoryGoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGoEvent from a JSON string
advisory_go_event_instance = AdvisoryGoEvent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGoEvent.to_json())

# convert the object into a dict
advisory_go_event_dict = advisory_go_event_instance.to_dict()
# create an instance of AdvisoryGoEvent from a dict
advisory_go_event_from_dict = AdvisoryGoEvent.from_dict(advisory_go_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


