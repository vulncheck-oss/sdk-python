# AdvisoryAnthropicCVD

advisory.AnthropicCVD

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution** | [**AdvisoryCredit**](AdvisoryCredit.md) |  | [optional] 
**bug_class** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_committed** | **str** |  | [optional] 
**entry** | **List[int]** |  | [optional] 
**ghsa** | **List[str]** |  | [optional] 
**hash** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**raw_preimage** | **List[int]** |  | [optional] 
**severities** | [**AdvisoryCVDSeverityCompare**](AdvisoryCVDSeverityCompare.md) |  | [optional] 
**snapshot** | [**AdvisoryCVDSnapshot**](AdvisoryCVDSnapshot.md) |  | [optional] 
**status** | **str** |  | [optional] 
**timeline** | [**List[AdvisoryTimeline]**](AdvisoryTimeline.md) | Timeline / Attribution / Severities come from the detail-page HTML (parsed at ingest, not from any JSON document). Revealed-only. | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_anthropic_cvd import AdvisoryAnthropicCVD

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAnthropicCVD from a JSON string
advisory_anthropic_cvd_instance = AdvisoryAnthropicCVD.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAnthropicCVD.to_json())

# convert the object into a dict
advisory_anthropic_cvd_dict = advisory_anthropic_cvd_instance.to_dict()
# create an instance of AdvisoryAnthropicCVD from a dict
advisory_anthropic_cvd_from_dict = AdvisoryAnthropicCVD.from_dict(advisory_anthropic_cvd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


