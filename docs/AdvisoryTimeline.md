# AdvisoryTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**time** | **str** | FIXME: flip to time | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_timeline import AdvisoryTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTimeline from a JSON string
advisory_timeline_instance = AdvisoryTimeline.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTimeline.to_json())

# convert the object into a dict
advisory_timeline_dict = advisory_timeline_instance.to_dict()
# create an instance of AdvisoryTimeline from a dict
advisory_timeline_from_dict = AdvisoryTimeline.from_dict(advisory_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


