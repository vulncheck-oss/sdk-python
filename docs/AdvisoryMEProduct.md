# AdvisoryMEProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_me_product import AdvisoryMEProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMEProduct from a JSON string
advisory_me_product_instance = AdvisoryMEProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMEProduct.to_json())

# convert the object into a dict
advisory_me_product_dict = advisory_me_product_instance.to_dict()
# create an instance of AdvisoryMEProduct from a dict
advisory_me_product_from_dict = AdvisoryMEProduct.from_dict(advisory_me_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


