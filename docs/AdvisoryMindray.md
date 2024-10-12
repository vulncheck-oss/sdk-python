# AdvisoryMindray


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
from vulncheck_sdk.models.advisory_mindray import AdvisoryMindray

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMindray from a JSON string
advisory_mindray_instance = AdvisoryMindray.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMindray.to_json())

# convert the object into a dict
advisory_mindray_dict = advisory_mindray_instance.to_dict()
# create an instance of AdvisoryMindray from a dict
advisory_mindray_from_dict = AdvisoryMindray.from_dict(advisory_mindray_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


