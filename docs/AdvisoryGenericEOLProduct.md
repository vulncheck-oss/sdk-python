# AdvisoryGenericEOLProduct

advisory.GenericEOLProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** |  | [optional] 
**product_version** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_generic_eol_product import AdvisoryGenericEOLProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGenericEOLProduct from a JSON string
advisory_generic_eol_product_instance = AdvisoryGenericEOLProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGenericEOLProduct.to_json())

# convert the object into a dict
advisory_generic_eol_product_dict = advisory_generic_eol_product_instance.to_dict()
# create an instance of AdvisoryGenericEOLProduct from a dict
advisory_generic_eol_product_from_dict = AdvisoryGenericEOLProduct.from_dict(advisory_generic_eol_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


