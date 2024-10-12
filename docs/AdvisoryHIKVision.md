# AdvisoryHIKVision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hik_vision import AdvisoryHIKVision

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHIKVision from a JSON string
advisory_hik_vision_instance = AdvisoryHIKVision.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHIKVision.to_json())

# convert the object into a dict
advisory_hik_vision_dict = advisory_hik_vision_instance.to_dict()
# create an instance of AdvisoryHIKVision from a dict
advisory_hik_vision_from_dict = AdvisoryHIKVision.from_dict(advisory_hik_vision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


