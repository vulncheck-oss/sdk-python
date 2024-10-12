# AdvisoryHaskellSADBAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**affected_packages** | [**List[AdvisoryHaskellSADBAffected]**](AdvisoryHaskellSADBAffected.md) |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**cves** | **List[str]** |  | [optional] 
**cwes** | **List[int]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**references** | **Dict[str, List[str]]** |  | [optional] 
**related_vulns** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_haskell_sadb_advisory import AdvisoryHaskellSADBAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHaskellSADBAdvisory from a JSON string
advisory_haskell_sadb_advisory_instance = AdvisoryHaskellSADBAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHaskellSADBAdvisory.to_json())

# convert the object into a dict
advisory_haskell_sadb_advisory_dict = advisory_haskell_sadb_advisory_instance.to_dict()
# create an instance of AdvisoryHaskellSADBAdvisory from a dict
advisory_haskell_sadb_advisory_from_dict = AdvisoryHaskellSADBAdvisory.from_dict(advisory_haskell_sadb_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


