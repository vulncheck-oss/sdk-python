# AdvisoryVulnrichmentOther


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**AdvisoryVulnrichmentContent**](AdvisoryVulnrichmentContent.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnrichment_other import AdvisoryVulnrichmentOther

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnrichmentOther from a JSON string
advisory_vulnrichment_other_instance = AdvisoryVulnrichmentOther.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnrichmentOther.to_json())

# convert the object into a dict
advisory_vulnrichment_other_dict = advisory_vulnrichment_other_instance.to_dict()
# create an instance of AdvisoryVulnrichmentOther from a dict
advisory_vulnrichment_other_from_dict = AdvisoryVulnrichmentOther.from_dict(advisory_vulnrichment_other_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


