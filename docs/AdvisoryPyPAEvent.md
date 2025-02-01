# AdvisoryPyPAEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed** | **str** |  | [optional] 
**introduced** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_py_pa_event import AdvisoryPyPAEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPyPAEvent from a JSON string
advisory_py_pa_event_instance = AdvisoryPyPAEvent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPyPAEvent.to_json())

# convert the object into a dict
advisory_py_pa_event_dict = advisory_py_pa_event_instance.to_dict()
# create an instance of AdvisoryPyPAEvent from a dict
advisory_py_pa_event_from_dict = AdvisoryPyPAEvent.from_dict(advisory_py_pa_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


