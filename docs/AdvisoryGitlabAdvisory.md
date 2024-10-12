# AdvisoryGitlabAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_range** | **str** |  | [optional] 
**affected_versions** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_v2** | **str** |  | [optional] 
**cvss_v3** | **str** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**var_date** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**fixed_versions** | **List[str]** |  | [optional] 
**ghsa** | **List[str]** |  | [optional] 
**gitlab_url** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**identifiers** | **List[str]** |  | [optional] 
**not_impacted** | **str** |  | [optional] 
**package_manager** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**package_slug** | **str** |  | [optional] 
**pubdate** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**urls** | **List[str]** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gitlab_advisory import AdvisoryGitlabAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGitlabAdvisory from a JSON string
advisory_gitlab_advisory_instance = AdvisoryGitlabAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGitlabAdvisory.to_json())

# convert the object into a dict
advisory_gitlab_advisory_dict = advisory_gitlab_advisory_instance.to_dict()
# create an instance of AdvisoryGitlabAdvisory from a dict
advisory_gitlab_advisory_from_dict = AdvisoryGitlabAdvisory.from_dict(advisory_gitlab_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


