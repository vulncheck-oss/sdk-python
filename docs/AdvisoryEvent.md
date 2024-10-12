# AdvisoryEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed** | **str** |  | [optional] 
**introduced** | **str** |  | [optional] 
**last_affected** | **str** |  | [optional] 
**limit** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_event import AdvisoryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEvent from a JSON string
advisory_event_instance = AdvisoryEvent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEvent.to_json())

# convert the object into a dict
advisory_event_dict = advisory_event_instance.to_dict()
# create an instance of AdvisoryEvent from a dict
advisory_event_from_dict = AdvisoryEvent.from_dict(advisory_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


