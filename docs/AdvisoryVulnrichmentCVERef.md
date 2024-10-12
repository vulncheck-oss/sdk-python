# AdvisoryVulnrichmentCVERef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**AdvisoryVulnrichmentContainers**](AdvisoryVulnrichmentContainers.md) |  | [optional] 
**cve_metadata** | [**AdvisoryMCveMetadata**](AdvisoryMCveMetadata.md) |  | [optional] 
**data_type** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnrichment_cve_ref import AdvisoryVulnrichmentCVERef

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnrichmentCVERef from a JSON string
advisory_vulnrichment_cve_ref_instance = AdvisoryVulnrichmentCVERef.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnrichmentCVERef.to_json())

# convert the object into a dict
advisory_vulnrichment_cve_ref_dict = advisory_vulnrichment_cve_ref_instance.to_dict()
# create an instance of AdvisoryVulnrichmentCVERef from a dict
advisory_vulnrichment_cve_ref_from_dict = AdvisoryVulnrichmentCVERef.from_dict(advisory_vulnrichment_cve_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


