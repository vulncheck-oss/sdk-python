# ApiOSSPackageArtifacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary** | [**List[ApiOSSPackageDownloadInfo]**](ApiOSSPackageDownloadInfo.md) |  | [optional] 
**source** | [**List[ApiOSSPackageDownloadInfo]**](ApiOSSPackageDownloadInfo.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_oss_package_artifacts import ApiOSSPackageArtifacts

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOSSPackageArtifacts from a JSON string
api_oss_package_artifacts_instance = ApiOSSPackageArtifacts.from_json(json)
# print the JSON string representation of the object
print(ApiOSSPackageArtifacts.to_json())

# convert the object into a dict
api_oss_package_artifacts_dict = api_oss_package_artifacts_instance.to_dict()
# create an instance of ApiOSSPackageArtifacts from a dict
api_oss_package_artifacts_from_dict = ApiOSSPackageArtifacts.from_dict(api_oss_package_artifacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


