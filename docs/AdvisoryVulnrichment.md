# AdvisoryVulnrichment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**mitre_ref** | [**AdvisoryVulnrichmentCVERef**](AdvisoryVulnrichmentCVERef.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnrichment import AdvisoryVulnrichment

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnrichment from a JSON string
advisory_vulnrichment_instance = AdvisoryVulnrichment.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnrichment.to_json())

# convert the object into a dict
advisory_vulnrichment_dict = advisory_vulnrichment_instance.to_dict()
# create an instance of AdvisoryVulnrichment from a dict
advisory_vulnrichment_from_dict = AdvisoryVulnrichment.from_dict(advisory_vulnrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


