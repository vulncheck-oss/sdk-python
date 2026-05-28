# AdvisoryMCna

advisory.MCna

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryMAffected]**](AdvisoryMAffected.md) |  | [optional] 
**configurations** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**cpe_applicability** | [**List[AdvisoryCustomCPE]**](AdvisoryCustomCPE.md) |  | [optional] 
**credits** | [**List[AdvisoryCredit]**](AdvisoryCredit.md) |  | [optional] 
**date_assigned** | **str** |  | [optional] 
**date_public** | **str** |  | [optional] 
**descriptions** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**exploits** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**impacts** | [**List[AdvisoryImpact]**](AdvisoryImpact.md) |  | [optional] 
**metrics** | [**List[AdvisoryMetric]**](AdvisoryMetric.md) |  | [optional] 
**problem_types** | [**List[AdvisoryMProblemTypes]**](AdvisoryMProblemTypes.md) |  | [optional] 
**provider_metadata** | [**AdvisoryMProviderMetadata**](AdvisoryMProviderMetadata.md) |  | [optional] 
**references** | [**List[AdvisoryMReference]**](AdvisoryMReference.md) |  | [optional] 
**rejected_reasons** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) | Fields below appear only on rejected records (cveMetadata.state &#x3D;&#x3D; \&quot;REJECTED\&quot;). | [optional] 
**replaced_by** | **List[str]** |  | [optional] 
**solutions** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**source** | **List[int]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**taxonomy_mappings** | [**List[AdvisoryTaxonomyMapping]**](AdvisoryTaxonomyMapping.md) |  | [optional] 
**timeline** | [**List[AdvisoryTimeline]**](AdvisoryTimeline.md) |  | [optional] 
**title** | **str** |  | [optional] 
**workarounds** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 

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


