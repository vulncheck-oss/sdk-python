# ApiNVD20AffectedVersion

api.NVD20AffectedVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[ApiNVD20AffectedVersionChange]**](ApiNVD20AffectedVersionChange.md) |  | [optional] 
**less_than** | **str** |  | [optional] 
**less_than_or_equal** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**version_type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_affected_version import ApiNVD20AffectedVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20AffectedVersion from a JSON string
api_nvd20_affected_version_instance = ApiNVD20AffectedVersion.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20AffectedVersion.to_json())

# convert the object into a dict
api_nvd20_affected_version_dict = api_nvd20_affected_version_instance.to_dict()
# create an instance of ApiNVD20AffectedVersion from a dict
api_nvd20_affected_version_from_dict = ApiNVD20AffectedVersion.from_dict(api_nvd20_affected_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


