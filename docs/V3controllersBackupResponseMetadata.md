# V3controllersBackupResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.v3controllers_backup_response_metadata import V3controllersBackupResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of V3controllersBackupResponseMetadata from a JSON string
v3controllers_backup_response_metadata_instance = V3controllersBackupResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(V3controllersBackupResponseMetadata.to_json())

# convert the object into a dict
v3controllers_backup_response_metadata_dict = v3controllers_backup_response_metadata_instance.to_dict()
# create an instance of V3controllersBackupResponseMetadata from a dict
v3controllers_backup_response_metadata_from_dict = V3controllersBackupResponseMetadata.from_dict(v3controllers_backup_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


