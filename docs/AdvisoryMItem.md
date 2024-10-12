# AdvisoryMItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AdvisoryMItem]**](AdvisoryMItem.md) |  | [optional] 
**name** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**type** | **int** | diff | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_item import AdvisoryMItem

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMItem from a JSON string
advisory_m_item_instance = AdvisoryMItem.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMItem.to_json())

# convert the object into a dict
advisory_m_item_dict = advisory_m_item_instance.to_dict()
# create an instance of AdvisoryMItem from a dict
advisory_m_item_from_dict = AdvisoryMItem.from_dict(advisory_m_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


