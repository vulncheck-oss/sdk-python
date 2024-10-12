# AdvisoryAffectedProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_releases** | **str** |  | [optional] 
**fixed_releases** | **str** |  | [optional] 
**lexmark_models** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected_product import AdvisoryAffectedProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffectedProduct from a JSON string
advisory_affected_product_instance = AdvisoryAffectedProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffectedProduct.to_json())

# convert the object into a dict
advisory_affected_product_dict = advisory_affected_product_instance.to_dict()
# create an instance of AdvisoryAffectedProduct from a dict
advisory_affected_product_from_dict = AdvisoryAffectedProduct.from_dict(advisory_affected_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


