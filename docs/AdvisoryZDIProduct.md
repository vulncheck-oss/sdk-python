# AdvisoryZDIProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**vendor** | [**AdvisoryZDIVendor**](AdvisoryZDIVendor.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zdi_product import AdvisoryZDIProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZDIProduct from a JSON string
advisory_zdi_product_instance = AdvisoryZDIProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZDIProduct.to_json())

# convert the object into a dict
advisory_zdi_product_dict = advisory_zdi_product_instance.to_dict()
# create an instance of AdvisoryZDIProduct from a dict
advisory_zdi_product_from_dict = AdvisoryZDIProduct.from_dict(advisory_zdi_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


