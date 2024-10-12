# AdvisoryBinarly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_binarly import AdvisoryBinarly

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBinarly from a JSON string
advisory_binarly_instance = AdvisoryBinarly.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBinarly.to_json())

# convert the object into a dict
advisory_binarly_dict = advisory_binarly_instance.to_dict()
# create an instance of AdvisoryBinarly from a dict
advisory_binarly_from_dict = AdvisoryBinarly.from_dict(advisory_binarly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


