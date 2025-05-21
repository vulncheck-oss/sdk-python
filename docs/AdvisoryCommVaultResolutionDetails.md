# AdvisoryCommVaultResolutionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_release** | **str** |  | [optional] 
**maintenance_release** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_comm_vault_resolution_details import AdvisoryCommVaultResolutionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCommVaultResolutionDetails from a JSON string
advisory_comm_vault_resolution_details_instance = AdvisoryCommVaultResolutionDetails.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCommVaultResolutionDetails.to_json())

# convert the object into a dict
advisory_comm_vault_resolution_details_dict = advisory_comm_vault_resolution_details_instance.to_dict()
# create an instance of AdvisoryCommVaultResolutionDetails from a dict
advisory_comm_vault_resolution_details_from_dict = AdvisoryCommVaultResolutionDetails.from_dict(advisory_comm_vault_resolution_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


