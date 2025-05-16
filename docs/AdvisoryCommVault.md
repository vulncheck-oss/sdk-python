# AdvisoryCommVault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cve_details** | [**List[AdvisoryCommVaultCVEDetails]**](AdvisoryCommVaultCVEDetails.md) |  | [optional] 
**cvss_range** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**impacted_product** | [**AdvisoryCommVaultImpactedProduct**](AdvisoryCommVaultImpactedProduct.md) |  | [optional] 
**references** | **List[str]** |  | [optional] 
**resolution** | [**AdvisoryCommVaultResolution**](AdvisoryCommVaultResolution.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_comm_vault import AdvisoryCommVault

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCommVault from a JSON string
advisory_comm_vault_instance = AdvisoryCommVault.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCommVault.to_json())

# convert the object into a dict
advisory_comm_vault_dict = advisory_comm_vault_instance.to_dict()
# create an instance of AdvisoryCommVault from a dict
advisory_comm_vault_from_dict = AdvisoryCommVault.from_dict(advisory_comm_vault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


