# AdvisoryVulnrichmentContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**options** | [**List[AdvisoryVulnrichmentOption]**](AdvisoryVulnrichmentOption.md) |  | [optional] 
**role** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnrichment_content import AdvisoryVulnrichmentContent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnrichmentContent from a JSON string
advisory_vulnrichment_content_instance = AdvisoryVulnrichmentContent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnrichmentContent.to_json())

# convert the object into a dict
advisory_vulnrichment_content_dict = advisory_vulnrichment_content_instance.to_dict()
# create an instance of AdvisoryVulnrichmentContent from a dict
advisory_vulnrichment_content_from_dict = AdvisoryVulnrichmentContent.from_dict(advisory_vulnrichment_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


