# AdvisoryADPContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryMAffected]**](AdvisoryMAffected.md) |  | [optional] 
**date_public** | **str** | OK | [optional] 
**descriptions** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) | OK | [optional] 
**impacts** | [**List[AdvisoryImpact]**](AdvisoryImpact.md) | OK | [optional] 
**metrics** | [**List[AdvisoryMetric]**](AdvisoryMetric.md) | OK | [optional] 
**problem_types** | [**List[AdvisoryMProblemTypes]**](AdvisoryMProblemTypes.md) | OK | [optional] 
**provider_metadata** | [**AdvisoryMProviderMetadata**](AdvisoryMProviderMetadata.md) | OK | [optional] 
**references** | [**List[AdvisoryMReference]**](AdvisoryMReference.md) |  | [optional] 
**tags** | **List[str]** | OK | [optional] 
**title** | **str** | OK | [optional] 

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


