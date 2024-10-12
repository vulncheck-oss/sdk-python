# AdvisoryMISPValueNoID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**meta** | [**AdvisoryMispMeta**](AdvisoryMispMeta.md) |  | [optional] 
**related** | [**List[AdvisoryMispRelatedItem]**](AdvisoryMispRelatedItem.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_misp_value_no_id import AdvisoryMISPValueNoID

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMISPValueNoID from a JSON string
advisory_misp_value_no_id_instance = AdvisoryMISPValueNoID.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMISPValueNoID.to_json())

# convert the object into a dict
advisory_misp_value_no_id_dict = advisory_misp_value_no_id_instance.to_dict()
# create an instance of AdvisoryMISPValueNoID from a dict
advisory_misp_value_no_id_from_dict = AdvisoryMISPValueNoID.from_dict(advisory_misp_value_no_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


