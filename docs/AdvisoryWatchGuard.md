# AdvisoryWatchGuard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**score** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_watch_guard import AdvisoryWatchGuard

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWatchGuard from a JSON string
advisory_watch_guard_instance = AdvisoryWatchGuard.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWatchGuard.to_json())

# convert the object into a dict
advisory_watch_guard_dict = advisory_watch_guard_instance.to_dict()
# create an instance of AdvisoryWatchGuard from a dict
advisory_watch_guard_from_dict = AdvisoryWatchGuard.from_dict(advisory_watch_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


