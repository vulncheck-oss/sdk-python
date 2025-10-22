# AdvisoryGHSADatabaseSpecific


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwe_ids** | **List[str]** |  | [optional] 
**github_reviewed** | **bool** |  | [optional] 
**github_reviewed_at** | **str** |  | [optional] 
**nvd_published_at** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ghsa_database_specific import AdvisoryGHSADatabaseSpecific

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHSADatabaseSpecific from a JSON string
advisory_ghsa_database_specific_instance = AdvisoryGHSADatabaseSpecific.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHSADatabaseSpecific.to_json())

# convert the object into a dict
advisory_ghsa_database_specific_dict = advisory_ghsa_database_specific_instance.to_dict()
# create an instance of AdvisoryGHSADatabaseSpecific from a dict
advisory_ghsa_database_specific_from_dict = AdvisoryGHSADatabaseSpecific.from_dict(advisory_ghsa_database_specific_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


