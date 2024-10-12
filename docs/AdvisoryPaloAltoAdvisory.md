# AdvisoryPaloAltoAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**applicable_versions** | **str** |  | [optional] 
**attack_complexity** | **str** |  | [optional] 
**attack_vector** | **str** |  | [optional] 
**availability_impact** | **str** |  | [optional] 
**confidentiality_impact** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvssbase_score** | **str** |  | [optional] 
**date_published** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**integrity_impact** | **str** |  | [optional] 
**privileges_required** | **str** |  | [optional] 
**problem** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**unaffected** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user_interaction** | **str** |  | [optional] 
**workaround** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_palo_alto_advisory import AdvisoryPaloAltoAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPaloAltoAdvisory from a JSON string
advisory_palo_alto_advisory_instance = AdvisoryPaloAltoAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPaloAltoAdvisory.to_json())

# convert the object into a dict
advisory_palo_alto_advisory_dict = advisory_palo_alto_advisory_instance.to_dict()
# create an instance of AdvisoryPaloAltoAdvisory from a dict
advisory_palo_alto_advisory_from_dict = AdvisoryPaloAltoAdvisory.from_dict(advisory_palo_alto_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


