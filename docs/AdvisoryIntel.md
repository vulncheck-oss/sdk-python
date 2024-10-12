# AdvisoryIntel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_intel import AdvisoryIntel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIntel from a JSON string
advisory_intel_instance = AdvisoryIntel.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIntel.to_json())

# convert the object into a dict
advisory_intel_dict = advisory_intel_instance.to_dict()
# create an instance of AdvisoryIntel from a dict
advisory_intel_from_dict = AdvisoryIntel.from_dict(advisory_intel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


