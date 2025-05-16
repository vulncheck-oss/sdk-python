# AdvisoryGoVulnAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_specific** | [**AdvisoryGoVulnDatabaseSpecific**](AdvisoryGoVulnDatabaseSpecific.md) |  | [optional] 
**ecosystem_specific** | [**AdvisoryGoVulnEcosystemSpecific**](AdvisoryGoVulnEcosystemSpecific.md) |  | [optional] 
**package** | [**AdvisoryGoVulnPackage**](AdvisoryGoVulnPackage.md) |  | [optional] 
**ranges** | [**List[AdvisoryGoVulnRanges]**](AdvisoryGoVulnRanges.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_go_vuln_affected import AdvisoryGoVulnAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGoVulnAffected from a JSON string
advisory_go_vuln_affected_instance = AdvisoryGoVulnAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGoVulnAffected.to_json())

# convert the object into a dict
advisory_go_vuln_affected_dict = advisory_go_vuln_affected_instance.to_dict()
# create an instance of AdvisoryGoVulnAffected from a dict
advisory_go_vuln_affected_from_dict = AdvisoryGoVulnAffected.from_dict(advisory_go_vuln_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


