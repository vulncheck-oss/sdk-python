# AdvisoryHaskellAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_constraint** | **str** |  | [optional] 
**affected_versions** | [**List[AdvisoryHaskellVersion]**](AdvisoryHaskellVersion.md) |  | [optional] 
**arch** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**os** | **List[str]** |  | [optional] 
**package** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_haskell_affected import AdvisoryHaskellAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHaskellAffected from a JSON string
advisory_haskell_affected_instance = AdvisoryHaskellAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHaskellAffected.to_json())

# convert the object into a dict
advisory_haskell_affected_dict = advisory_haskell_affected_instance.to_dict()
# create an instance of AdvisoryHaskellAffected from a dict
advisory_haskell_affected_from_dict = AdvisoryHaskellAffected.from_dict(advisory_haskell_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


