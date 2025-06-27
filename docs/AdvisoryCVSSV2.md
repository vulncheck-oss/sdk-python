# AdvisoryCVSSV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_complexity** | **str** |  | [optional] 
**access_vector** | **str** |  | [optional] 
**authentication** | **str** |  | [optional] 
**availability_impact** | **str** |  | [optional] 
**availability_requirement** | **str** |  | [optional] 
**base_score** | **float** |  | [optional] 
**collateral_damage_potential** | **str** |  | [optional] 
**confidentiality_impact** | **str** |  | [optional] 
**confidentiality_requirement** | **str** |  | [optional] 
**environmental_score** | **float** |  | [optional] 
**exploitability** | **str** |  | [optional] 
**integrity_impact** | **str** |  | [optional] 
**integrity_requirement** | **str** |  | [optional] 
**remediation_level** | **str** |  | [optional] 
**report_confidence** | **str** |  | [optional] 
**target_distribution** | **str** |  | [optional] 
**temporal_score** | **float** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvssv2 import AdvisoryCVSSV2

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVSSV2 from a JSON string
advisory_cvssv2_instance = AdvisoryCVSSV2.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVSSV2.to_json())

# convert the object into a dict
advisory_cvssv2_dict = advisory_cvssv2_instance.to_dict()
# create an instance of AdvisoryCVSSV2 from a dict
advisory_cvssv2_from_dict = AdvisoryCVSSV2.from_dict(advisory_cvssv2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


