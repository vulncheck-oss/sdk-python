# AdvisoryMispRelatedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_uuid** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_misp_related_item import AdvisoryMispRelatedItem

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMispRelatedItem from a JSON string
advisory_misp_related_item_instance = AdvisoryMispRelatedItem.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMispRelatedItem.to_json())

# convert the object into a dict
advisory_misp_related_item_dict = advisory_misp_related_item_instance.to_dict()
# create an instance of AdvisoryMispRelatedItem from a dict
advisory_misp_related_item_from_dict = AdvisoryMispRelatedItem.from_dict(advisory_misp_related_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


