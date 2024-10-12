# AdvisorySiemensProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_identification_helper** | [**AdvisorySiemensProductIdentificationHelper**](AdvisorySiemensProductIdentificationHelper.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_product import AdvisorySiemensProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensProduct from a JSON string
advisory_siemens_product_instance = AdvisorySiemensProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensProduct.to_json())

# convert the object into a dict
advisory_siemens_product_dict = advisory_siemens_product_instance.to_dict()
# create an instance of AdvisorySiemensProduct from a dict
advisory_siemens_product_from_dict = AdvisorySiemensProduct.from_dict(advisory_siemens_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


