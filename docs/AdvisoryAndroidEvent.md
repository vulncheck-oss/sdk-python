# AdvisoryAndroidEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed** | **str** |  | [optional] 
**introduced** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_android_event import AdvisoryAndroidEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAndroidEvent from a JSON string
advisory_android_event_instance = AdvisoryAndroidEvent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAndroidEvent.to_json())

# convert the object into a dict
advisory_android_event_dict = advisory_android_event_instance.to_dict()
# create an instance of AdvisoryAndroidEvent from a dict
advisory_android_event_from_dict = AdvisoryAndroidEvent.from_dict(advisory_android_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


