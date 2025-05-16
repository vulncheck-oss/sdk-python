# AdvisoryCommVaultCVEDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_id** | **str** |  | [optional] 
**cvss** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**external_links** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_comm_vault_cve_details import AdvisoryCommVaultCVEDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCommVaultCVEDetails from a JSON string
advisory_comm_vault_cve_details_instance = AdvisoryCommVaultCVEDetails.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCommVaultCVEDetails.to_json())

# convert the object into a dict
advisory_comm_vault_cve_details_dict = advisory_comm_vault_cve_details_instance.to_dict()
# create an instance of AdvisoryCommVaultCVEDetails from a dict
advisory_comm_vault_cve_details_from_dict = AdvisoryCommVaultCVEDetails.from_dict(advisory_comm_vault_cve_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


