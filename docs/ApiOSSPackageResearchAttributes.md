# ApiOSSPackageResearchAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned** | **bool** |  | [optional] 
**eol** | **bool** |  | [optional] 
**is_malicious** | **bool** |  | [optional] 
**malicious_source** | **str** |  | [optional] 
**repo_hijackable** | **bool** |  | [optional] 
**squatted_package** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_oss_package_research_attributes import ApiOSSPackageResearchAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOSSPackageResearchAttributes from a JSON string
api_oss_package_research_attributes_instance = ApiOSSPackageResearchAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiOSSPackageResearchAttributes.to_json())

# convert the object into a dict
api_oss_package_research_attributes_dict = api_oss_package_research_attributes_instance.to_dict()
# create an instance of ApiOSSPackageResearchAttributes from a dict
api_oss_package_research_attributes_from_dict = ApiOSSPackageResearchAttributes.from_dict(api_oss_package_research_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


