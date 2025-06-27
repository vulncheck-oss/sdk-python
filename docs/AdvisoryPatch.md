# AdvisoryPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**component** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**os_sw** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_patch import AdvisoryPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPatch from a JSON string
advisory_patch_instance = AdvisoryPatch.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPatch.to_json())

# convert the object into a dict
advisory_patch_dict = advisory_patch_instance.to_dict()
# create an instance of AdvisoryPatch from a dict
advisory_patch_from_dict = AdvisoryPatch.from_dict(advisory_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


