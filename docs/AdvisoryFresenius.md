# AdvisoryFresenius


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_fresenius import AdvisoryFresenius

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFresenius from a JSON string
advisory_fresenius_instance = AdvisoryFresenius.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFresenius.to_json())

# convert the object into a dict
advisory_fresenius_dict = advisory_fresenius_instance.to_dict()
# create an instance of AdvisoryFresenius from a dict
advisory_fresenius_from_dict = AdvisoryFresenius.from_dict(advisory_fresenius_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


