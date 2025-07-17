# AdvisoryVulnerableProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnerable_product import AdvisoryVulnerableProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnerableProduct from a JSON string
advisory_vulnerable_product_instance = AdvisoryVulnerableProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnerableProduct.to_json())

# convert the object into a dict
advisory_vulnerable_product_dict = advisory_vulnerable_product_instance.to_dict()
# create an instance of AdvisoryVulnerableProduct from a dict
advisory_vulnerable_product_from_dict = AdvisoryVulnerableProduct.from_dict(advisory_vulnerable_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


