# AdvisoryDistroPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary** | **bool** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**license** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**sec_fixes** | [**List[AdvisorySecFix]**](AdvisorySecFix.md) |  | [optional] 
**versions** | [**List[AdvisoryDistroVersion]**](AdvisoryDistroVersion.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_distro_package import AdvisoryDistroPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDistroPackage from a JSON string
advisory_distro_package_instance = AdvisoryDistroPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDistroPackage.to_json())

# convert the object into a dict
advisory_distro_package_dict = advisory_distro_package_instance.to_dict()
# create an instance of AdvisoryDistroPackage from a dict
advisory_distro_package_from_dict = AdvisoryDistroPackage.from_dict(advisory_distro_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


