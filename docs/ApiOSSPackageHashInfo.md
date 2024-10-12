# ApiOSSPackageHashInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | See OSSPackageHashInfoAlgo* consts | [optional] 
**type** | **str** | See OSSPackageHashInfoType* consts | [optional] 
**value** | **str** | hex string digest or link to hash | [optional] 

## Example

```python
from vulncheck_sdk.models.api_oss_package_hash_info import ApiOSSPackageHashInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOSSPackageHashInfo from a JSON string
api_oss_package_hash_info_instance = ApiOSSPackageHashInfo.from_json(json)
# print the JSON string representation of the object
print(ApiOSSPackageHashInfo.to_json())

# convert the object into a dict
api_oss_package_hash_info_dict = api_oss_package_hash_info_instance.to_dict()
# create an instance of ApiOSSPackageHashInfo from a dict
api_oss_package_hash_info_from_dict = ApiOSSPackageHashInfo.from_dict(api_oss_package_hash_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


