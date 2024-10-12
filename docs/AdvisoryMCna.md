# AdvisoryMCna


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryMAffected]**](AdvisoryMAffected.md) |  | [optional] 
**credits** | [**List[AdvisoryCredit]**](AdvisoryCredit.md) |  | [optional] 
**descriptions** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**metrics** | [**List[AdvisoryMetric]**](AdvisoryMetric.md) |  | [optional] 
**problem_types** | [**List[AdvisoryMProblemTypes]**](AdvisoryMProblemTypes.md) |  | [optional] 
**provider_metadata** | [**AdvisoryMProviderMetadata**](AdvisoryMProviderMetadata.md) |  | [optional] 
**references** | [**List[AdvisoryMReference]**](AdvisoryMReference.md) |  | [optional] 
**timeline** | [**List[AdvisoryTimeline]**](AdvisoryTimeline.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_cna import AdvisoryMCna

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMCna from a JSON string
advisory_m_cna_instance = AdvisoryMCna.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMCna.to_json())

# convert the object into a dict
advisory_m_cna_dict = advisory_m_cna_instance.to_dict()
# create an instance of AdvisoryMCna from a dict
advisory_m_cna_from_dict = AdvisoryMCna.from_dict(advisory_m_cna_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


