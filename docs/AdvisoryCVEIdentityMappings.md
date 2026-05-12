# AdvisoryCVEIdentityMappings

advisory.CVEIdentityMappings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**mappings** | [**List[AdvisoryCVEMapping]**](AdvisoryCVEMapping.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cve_identity_mappings import AdvisoryCVEIdentityMappings

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVEIdentityMappings from a JSON string
advisory_cve_identity_mappings_instance = AdvisoryCVEIdentityMappings.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVEIdentityMappings.to_json())

# convert the object into a dict
advisory_cve_identity_mappings_dict = advisory_cve_identity_mappings_instance.to_dict()
# create an instance of AdvisoryCVEIdentityMappings from a dict
advisory_cve_identity_mappings_from_dict = AdvisoryCVEIdentityMappings.from_dict(advisory_cve_identity_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


