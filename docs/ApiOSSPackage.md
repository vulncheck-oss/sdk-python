# ApiOSSPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | [**ApiOSSPackageArtifacts**](ApiOSSPackageArtifacts.md) |  | [optional] 
**cves** | **List[str]** |  | [optional] 
**licenses** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**published_date** | **str** |  | [optional] 
**purl** | **List[str]** |  | [optional] 
**research_attributes** | [**ApiOSSPackageResearchAttributes**](ApiOSSPackageResearchAttributes.md) |  | [optional] 
**version** | **str** |  | [optional] 
**vulnerabilities** | [**List[ApiOSSPackageVulnerability]**](ApiOSSPackageVulnerability.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_oss_package import ApiOSSPackage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOSSPackage from a JSON string
api_oss_package_instance = ApiOSSPackage.from_json(json)
# print the JSON string representation of the object
print(ApiOSSPackage.to_json())

# convert the object into a dict
api_oss_package_dict = api_oss_package_instance.to_dict()
# create an instance of ApiOSSPackage from a dict
api_oss_package_from_dict = ApiOSSPackage.from_dict(api_oss_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


