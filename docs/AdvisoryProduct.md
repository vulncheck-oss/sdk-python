# AdvisoryProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_identification_helper** | **Dict[str, str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_product import AdvisoryProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryProduct from a JSON string
advisory_product_instance = AdvisoryProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryProduct.to_json())

# convert the object into a dict
advisory_product_dict = advisory_product_instance.to_dict()
# create an instance of AdvisoryProduct from a dict
advisory_product_from_dict = AdvisoryProduct.from_dict(advisory_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


