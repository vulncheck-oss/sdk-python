# ApiNVD20AffectedVersionChange

api.NVD20AffectedVersionChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_affected_version_change import ApiNVD20AffectedVersionChange

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20AffectedVersionChange from a JSON string
api_nvd20_affected_version_change_instance = ApiNVD20AffectedVersionChange.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20AffectedVersionChange.to_json())

# convert the object into a dict
api_nvd20_affected_version_change_dict = api_nvd20_affected_version_change_instance.to_dict()
# create an instance of ApiNVD20AffectedVersionChange from a dict
api_nvd20_affected_version_change_from_dict = ApiNVD20AffectedVersionChange.from_dict(api_nvd20_affected_version_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


