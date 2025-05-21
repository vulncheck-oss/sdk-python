# AdvisoryEnisaIDProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_enisa_id_product import AdvisoryEnisaIDProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEnisaIDProduct from a JSON string
advisory_enisa_id_product_instance = AdvisoryEnisaIDProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEnisaIDProduct.to_json())

# convert the object into a dict
advisory_enisa_id_product_dict = advisory_enisa_id_product_instance.to_dict()
# create an instance of AdvisoryEnisaIDProduct from a dict
advisory_enisa_id_product_from_dict = AdvisoryEnisaIDProduct.from_dict(advisory_enisa_id_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


