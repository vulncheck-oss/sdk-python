# AdvisoryCommVaultImpactedProductDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_versions** | **str** |  | [optional] 
**platforms** | **List[str]** |  | [optional] 
**product_name** | **str** |  | [optional] 
**resolved_versions** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_comm_vault_impacted_product_details import AdvisoryCommVaultImpactedProductDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCommVaultImpactedProductDetails from a JSON string
advisory_comm_vault_impacted_product_details_instance = AdvisoryCommVaultImpactedProductDetails.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCommVaultImpactedProductDetails.to_json())

# convert the object into a dict
advisory_comm_vault_impacted_product_details_dict = advisory_comm_vault_impacted_product_details_instance.to_dict()
# create an instance of AdvisoryCommVaultImpactedProductDetails from a dict
advisory_comm_vault_impacted_product_details_from_dict = AdvisoryCommVaultImpactedProductDetails.from_dict(advisory_comm_vault_impacted_product_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


