# AdvisoryADPContainer

advisory.ADPContainer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryMAffected]**](AdvisoryMAffected.md) |  | [optional] 
**configurations** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**cpe_applicability** | [**List[AdvisoryCustomCPE]**](AdvisoryCustomCPE.md) |  | [optional] 
**credits** | [**List[AdvisoryCredit]**](AdvisoryCredit.md) |  | [optional] 
**date_public** | **str** |  | [optional] 
**descriptions** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**exploits** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**impacts** | [**List[AdvisoryImpact]**](AdvisoryImpact.md) |  | [optional] 
**metrics** | [**List[AdvisoryMetric]**](AdvisoryMetric.md) |  | [optional] 
**problem_types** | [**List[AdvisoryMProblemTypes]**](AdvisoryMProblemTypes.md) |  | [optional] 
**provider_metadata** | [**AdvisoryMProviderMetadata**](AdvisoryMProviderMetadata.md) |  | [optional] 
**references** | [**List[AdvisoryMReference]**](AdvisoryMReference.md) |  | [optional] 
**solutions** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 
**source** | **List[int]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**taxonomy_mappings** | [**List[AdvisoryTaxonomyMapping]**](AdvisoryTaxonomyMapping.md) |  | [optional] 
**timeline** | [**List[AdvisoryTimeline]**](AdvisoryTimeline.md) |  | [optional] 
**title** | **str** |  | [optional] 
**workarounds** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_adp_container import AdvisoryADPContainer

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryADPContainer from a JSON string
advisory_adp_container_instance = AdvisoryADPContainer.from_json(json)
# print the JSON string representation of the object
print(AdvisoryADPContainer.to_json())

# convert the object into a dict
advisory_adp_container_dict = advisory_adp_container_instance.to_dict()
# create an instance of AdvisoryADPContainer from a dict
advisory_adp_container_from_dict = AdvisoryADPContainer.from_dict(advisory_adp_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


