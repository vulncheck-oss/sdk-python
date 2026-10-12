# ApiNVD20CVETag

api.NVD20CVETag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_identifier** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cve_tag import ApiNVD20CVETag

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CVETag from a JSON string
api_nvd20_cve_tag_instance = ApiNVD20CVETag.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CVETag.to_json())

# convert the object into a dict
api_nvd20_cve_tag_dict = api_nvd20_cve_tag_instance.to_dict()
# create an instance of ApiNVD20CVETag from a dict
api_nvd20_cve_tag_from_dict = ApiNVD20CVETag.from_dict(api_nvd20_cve_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


