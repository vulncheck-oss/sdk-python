# BackupBackupResponse

backup.BackupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** |  | [optional] 
**feed** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**url_ap_southeast_2** | **str** |  | [optional] 
**url_eu_west_2** | **str** |  | [optional] 
**url_expires** | **str** |  | [optional] 
**url_mrap** | **str** |  | [optional] 
**url_ttl_minutes** | **int** |  | [optional] 
**url_us_east_1** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.backup_backup_response import BackupBackupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackupBackupResponse from a JSON string
backup_backup_response_instance = BackupBackupResponse.from_json(json)
# print the JSON string representation of the object
print(BackupBackupResponse.to_json())

# convert the object into a dict
backup_backup_response_dict = backup_backup_response_instance.to_dict()
# create an instance of BackupBackupResponse from a dict
backup_backup_response_from_dict = BackupBackupResponse.from_dict(backup_backup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


