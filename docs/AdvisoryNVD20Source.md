# AdvisoryNVD20Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_email** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**cwe_acceptance_level** | [**AdvisoryCweAcceptanceLevel**](AdvisoryCweAcceptanceLevel.md) |  | [optional] 
**last_modified** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**source_identifiers** | **List[str]** |  | [optional] 
**v3_acceptance_level** | [**AdvisoryV3AcceptanceLevel**](AdvisoryV3AcceptanceLevel.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nvd20_source import AdvisoryNVD20Source

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNVD20Source from a JSON string
advisory_nvd20_source_instance = AdvisoryNVD20Source.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNVD20Source.to_json())

# convert the object into a dict
advisory_nvd20_source_dict = advisory_nvd20_source_instance.to_dict()
# create an instance of AdvisoryNVD20Source from a dict
advisory_nvd20_source_from_dict = AdvisoryNVD20Source.from_dict(advisory_nvd20_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


