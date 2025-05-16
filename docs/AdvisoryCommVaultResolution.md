# AdvisoryCommVaultResolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**resolution_details** | [**List[AdvisoryCommVaultResolutionDetails]**](AdvisoryCommVaultResolutionDetails.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_comm_vault_resolution import AdvisoryCommVaultResolution

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCommVaultResolution from a JSON string
advisory_comm_vault_resolution_instance = AdvisoryCommVaultResolution.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCommVaultResolution.to_json())

# convert the object into a dict
advisory_comm_vault_resolution_dict = advisory_comm_vault_resolution_instance.to_dict()
# create an instance of AdvisoryCommVaultResolution from a dict
advisory_comm_vault_resolution_from_dict = AdvisoryCommVaultResolution.from_dict(advisory_comm_vault_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


