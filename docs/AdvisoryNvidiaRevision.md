# AdvisoryNvidiaRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nvidia_revision import AdvisoryNvidiaRevision

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNvidiaRevision from a JSON string
advisory_nvidia_revision_instance = AdvisoryNvidiaRevision.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNvidiaRevision.to_json())

# convert the object into a dict
advisory_nvidia_revision_dict = advisory_nvidia_revision_instance.to_dict()
# create an instance of AdvisoryNvidiaRevision from a dict
advisory_nvidia_revision_from_dict = AdvisoryNvidiaRevision.from_dict(advisory_nvidia_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


