# AdvisoryRsync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rsync import AdvisoryRsync

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRsync from a JSON string
advisory_rsync_instance = AdvisoryRsync.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRsync.to_json())

# convert the object into a dict
advisory_rsync_dict = advisory_rsync_instance.to_dict()
# create an instance of AdvisoryRsync from a dict
advisory_rsync_from_dict = AdvisoryRsync.from_dict(advisory_rsync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


