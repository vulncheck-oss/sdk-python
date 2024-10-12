# ApiOSSPackageDownloadInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashes** | [**List[ApiOSSPackageHashInfo]**](ApiOSSPackageHashInfo.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**type** | **str** | See OSSPackageDownloadInfoType* consts | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_oss_package_download_info import ApiOSSPackageDownloadInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOSSPackageDownloadInfo from a JSON string
api_oss_package_download_info_instance = ApiOSSPackageDownloadInfo.from_json(json)
# print the JSON string representation of the object
print(ApiOSSPackageDownloadInfo.to_json())

# convert the object into a dict
api_oss_package_download_info_dict = api_oss_package_download_info_instance.to_dict()
# create an instance of ApiOSSPackageDownloadInfo from a dict
api_oss_package_download_info_from_dict = ApiOSSPackageDownloadInfo.from_dict(api_oss_package_download_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


