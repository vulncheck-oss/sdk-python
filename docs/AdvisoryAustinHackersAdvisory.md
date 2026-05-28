# AdvisoryAustinHackersAdvisory

advisory.AustinHackersAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **float** | From detail page (omitted for external-linked CVEs) | [optional] 
**cvss_vector** | **str** |  | [optional] 
**cwe** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gcve** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** | From index table | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_austin_hackers_advisory import AdvisoryAustinHackersAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAustinHackersAdvisory from a JSON string
advisory_austin_hackers_advisory_instance = AdvisoryAustinHackersAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAustinHackersAdvisory.to_json())

# convert the object into a dict
advisory_austin_hackers_advisory_dict = advisory_austin_hackers_advisory_instance.to_dict()
# create an instance of AdvisoryAustinHackersAdvisory from a dict
advisory_austin_hackers_advisory_from_dict = AdvisoryAustinHackersAdvisory.from_dict(advisory_austin_hackers_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


