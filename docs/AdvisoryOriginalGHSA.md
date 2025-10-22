# AdvisoryOriginalGHSA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryGHSAAffected]**](AdvisoryGHSAAffected.md) |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**database_specific** | [**AdvisoryGHSADatabaseSpecific**](AdvisoryGHSADatabaseSpecific.md) |  | [optional] 
**details** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**references** | [**List[AdvisoryGHSAReference]**](AdvisoryGHSAReference.md) |  | [optional] 
**schema_version** | **str** |  | [optional] 
**severity** | [**List[AdvisoryGHSASeverity]**](AdvisoryGHSASeverity.md) |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_original_ghsa import AdvisoryOriginalGHSA

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOriginalGHSA from a JSON string
advisory_original_ghsa_instance = AdvisoryOriginalGHSA.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOriginalGHSA.to_json())

# convert the object into a dict
advisory_original_ghsa_dict = advisory_original_ghsa_instance.to_dict()
# create an instance of AdvisoryOriginalGHSA from a dict
advisory_original_ghsa_from_dict = AdvisoryOriginalGHSA.from_dict(advisory_original_ghsa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


