# AdvisoryProductsAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_products_affected import AdvisoryProductsAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryProductsAffected from a JSON string
advisory_products_affected_instance = AdvisoryProductsAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryProductsAffected.to_json())

# convert the object into a dict
advisory_products_affected_dict = advisory_products_affected_instance.to_dict()
# create an instance of AdvisoryProductsAffected from a dict
advisory_products_affected_from_dict = AdvisoryProductsAffected.from_dict(advisory_products_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


