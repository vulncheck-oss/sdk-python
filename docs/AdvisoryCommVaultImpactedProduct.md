# AdvisoryCommVaultImpactedProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**impacted_product_details** | [**List[AdvisoryCommVaultImpactedProductDetails]**](AdvisoryCommVaultImpactedProductDetails.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_comm_vault_impacted_product import AdvisoryCommVaultImpactedProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCommVaultImpactedProduct from a JSON string
advisory_comm_vault_impacted_product_instance = AdvisoryCommVaultImpactedProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCommVaultImpactedProduct.to_json())

# convert the object into a dict
advisory_comm_vault_impacted_product_dict = advisory_comm_vault_impacted_product_instance.to_dict()
# create an instance of AdvisoryCommVaultImpactedProduct from a dict
advisory_comm_vault_impacted_product_from_dict = AdvisoryCommVaultImpactedProduct.from_dict(advisory_comm_vault_impacted_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


