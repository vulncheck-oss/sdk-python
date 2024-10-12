# ParamsIndexBackupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** | Href API endpoint URI to detailed backup information | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.params_index_backup_list import ParamsIndexBackupList

# TODO update the JSON string below
json = "{}"
# create an instance of ParamsIndexBackupList from a JSON string
params_index_backup_list_instance = ParamsIndexBackupList.from_json(json)
# print the JSON string representation of the object
print(ParamsIndexBackupList.to_json())

# convert the object into a dict
params_index_backup_list_dict = params_index_backup_list_instance.to_dict()
# create an instance of ParamsIndexBackupList from a dict
params_index_backup_list_from_dict = ParamsIndexBackupList.from_dict(params_index_backup_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


