# BackupListBackupsResponse

backup.ListBackupsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BackupFeedItem]**](BackupFeedItem.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.backup_list_backups_response import BackupListBackupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackupListBackupsResponse from a JSON string
backup_list_backups_response_instance = BackupListBackupsResponse.from_json(json)
# print the JSON string representation of the object
print(BackupListBackupsResponse.to_json())

# convert the object into a dict
backup_list_backups_response_dict = backup_list_backups_response_instance.to_dict()
# create an instance of BackupListBackupsResponse from a dict
backup_list_backups_response_from_dict = BackupListBackupsResponse.from_dict(backup_list_backups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


