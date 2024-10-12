# AdvisoryHaskellSADBAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_constraint** | **str** | We produce AffectedConstraint based on AffectedVersions | [optional] 
**affected_versions** | [**List[AdvisoryHaskellSADBVersion]**](AdvisoryHaskellSADBVersion.md) |  | [optional] 
**arch** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**os** | **List[str]** |  | [optional] 
**package** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_haskell_sadb_affected import AdvisoryHaskellSADBAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHaskellSADBAffected from a JSON string
advisory_haskell_sadb_affected_instance = AdvisoryHaskellSADBAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHaskellSADBAffected.to_json())

# convert the object into a dict
advisory_haskell_sadb_affected_dict = advisory_haskell_sadb_affected_instance.to_dict()
# create an instance of AdvisoryHaskellSADBAffected from a dict
advisory_haskell_sadb_affected_from_dict = AdvisoryHaskellSADBAffected.from_dict(advisory_haskell_sadb_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


