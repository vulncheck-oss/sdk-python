# AdvisoryVulnrichmentOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatable** | **str** |  | [optional] 
**exploitation** | **str** |  | [optional] 
**technical_impact** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnrichment_option import AdvisoryVulnrichmentOption

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnrichmentOption from a JSON string
advisory_vulnrichment_option_instance = AdvisoryVulnrichmentOption.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnrichmentOption.to_json())

# convert the object into a dict
advisory_vulnrichment_option_dict = advisory_vulnrichment_option_instance.to_dict()
# create an instance of AdvisoryVulnrichmentOption from a dict
advisory_vulnrichment_option_from_dict = AdvisoryVulnrichmentOption.from_dict(advisory_vulnrichment_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


