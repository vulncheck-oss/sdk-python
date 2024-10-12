# AdvisoryGHVulnerabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[AdvisoryGHNode]**](AdvisoryGHNode.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gh_vulnerabilities import AdvisoryGHVulnerabilities

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHVulnerabilities from a JSON string
advisory_gh_vulnerabilities_instance = AdvisoryGHVulnerabilities.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHVulnerabilities.to_json())

# convert the object into a dict
advisory_gh_vulnerabilities_dict = advisory_gh_vulnerabilities_instance.to_dict()
# create an instance of AdvisoryGHVulnerabilities from a dict
advisory_gh_vulnerabilities_from_dict = AdvisoryGHVulnerabilities.from_dict(advisory_gh_vulnerabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


