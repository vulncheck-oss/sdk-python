# AdvisoryMispValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**meta** | [**AdvisoryMispMeta**](AdvisoryMispMeta.md) |  | [optional] 
**related** | [**List[AdvisoryMispRelatedItem]**](AdvisoryMispRelatedItem.md) |  | [optional] 
**uuid** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_misp_value import AdvisoryMispValue

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMispValue from a JSON string
advisory_misp_value_instance = AdvisoryMispValue.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMispValue.to_json())

# convert the object into a dict
advisory_misp_value_dict = advisory_misp_value_instance.to_dict()
# create an instance of AdvisoryMispValue from a dict
advisory_misp_value_from_dict = AdvisoryMispValue.from_dict(advisory_misp_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


