# AdvisoryVendorProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vendor_product import AdvisoryVendorProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVendorProduct from a JSON string
advisory_vendor_product_instance = AdvisoryVendorProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVendorProduct.to_json())

# convert the object into a dict
advisory_vendor_product_dict = advisory_vendor_product_instance.to_dict()
# create an instance of AdvisoryVendorProduct from a dict
advisory_vendor_product_from_dict = AdvisoryVendorProduct.from_dict(advisory_vendor_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


