# ApiNVD20Affected

api.NVD20Affected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_data** | [**List[ApiNVD20AffectedProduct]**](ApiNVD20AffectedProduct.md) |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_affected import ApiNVD20Affected

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20Affected from a JSON string
api_nvd20_affected_instance = ApiNVD20Affected.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20Affected.to_json())

# convert the object into a dict
api_nvd20_affected_dict = api_nvd20_affected_instance.to_dict()
# create an instance of ApiNVD20Affected from a dict
api_nvd20_affected_from_dict = ApiNVD20Affected.from_dict(api_nvd20_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


