# AdvisoryMFullProductName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_full_product_name import AdvisoryMFullProductName

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMFullProductName from a JSON string
advisory_m_full_product_name_instance = AdvisoryMFullProductName.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMFullProductName.to_json())

# convert the object into a dict
advisory_m_full_product_name_dict = advisory_m_full_product_name_instance.to_dict()
# create an instance of AdvisoryMFullProductName from a dict
advisory_m_full_product_name_from_dict = AdvisoryMFullProductName.from_dict(advisory_m_full_product_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


