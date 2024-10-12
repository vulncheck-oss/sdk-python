# ApiCVEDataMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigner** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cve_data_meta import ApiCVEDataMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCVEDataMeta from a JSON string
api_cve_data_meta_instance = ApiCVEDataMeta.from_json(json)
# print the JSON string representation of the object
print(ApiCVEDataMeta.to_json())

# convert the object into a dict
api_cve_data_meta_dict = api_cve_data_meta_instance.to_dict()
# create an instance of ApiCVEDataMeta from a dict
api_cve_data_meta_from_dict = ApiCVEDataMeta.from_dict(api_cve_data_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


