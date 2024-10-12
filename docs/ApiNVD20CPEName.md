# ApiNVD20CPEName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_name** | **str** |  | [optional] 
**cpe_name_id** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cpe_name import ApiNVD20CPEName

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CPEName from a JSON string
api_nvd20_cpe_name_instance = ApiNVD20CPEName.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CPEName.to_json())

# convert the object into a dict
api_nvd20_cpe_name_dict = api_nvd20_cpe_name_instance.to_dict()
# create an instance of ApiNVD20CPEName from a dict
api_nvd20_cpe_name_from_dict = ApiNVD20CPEName.from_dict(api_nvd20_cpe_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


