# RenderResponseArrayParamsIndexBackupList

render.Response-array_params_IndexBackupList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** | Benchmark is the server-side processing time for the request in seconds. Example: 0.122322 &#x3D; approximately 122 milliseconds | [optional] 
**data** | [**List[ParamsIndexBackupList]**](ParamsIndexBackupList.md) | Data is the data returned by the endpoint | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_array_params_index_backup_list import RenderResponseArrayParamsIndexBackupList

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseArrayParamsIndexBackupList from a JSON string
render_response_array_params_index_backup_list_instance = RenderResponseArrayParamsIndexBackupList.from_json(json)
# print the JSON string representation of the object
print(RenderResponseArrayParamsIndexBackupList.to_json())

# convert the object into a dict
render_response_array_params_index_backup_list_dict = render_response_array_params_index_backup_list_instance.to_dict()
# create an instance of RenderResponseArrayParamsIndexBackupList from a dict
render_response_array_params_index_backup_list_from_dict = RenderResponseArrayParamsIndexBackupList.from_dict(render_response_array_params_index_backup_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


