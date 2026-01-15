# ParamsIndexBackup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_ap_southeast_2** | **str** |  | [optional] 
**url_eu_west_2** | **str** |  | [optional] 
**url_expires** | **str** |  | [optional] 
**url_il_central_1** | **str** |  | [optional] 
**url_me_central_1** | **str** |  | [optional] 
**url_mrap** | **str** |  | [optional] 
**url_ttl_minutes** | **int** |  | [optional] 
**url_us_east_1** | **str** |  | [optional] 
**url_us_west_2** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.params_index_backup import ParamsIndexBackup

# TODO update the JSON string below
json = "{}"
# create an instance of ParamsIndexBackup from a JSON string
params_index_backup_instance = ParamsIndexBackup.from_json(json)
# print the JSON string representation of the object
print(ParamsIndexBackup.to_json())

# convert the object into a dict
params_index_backup_dict = params_index_backup_instance.to_dict()
# create an instance of ParamsIndexBackup from a dict
params_index_backup_from_dict = ParamsIndexBackup.from_dict(params_index_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


