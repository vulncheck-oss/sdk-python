# AdvisoryCVSSV40


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatable** | **str** |  | [optional] 
**recovery** | **str** |  | [optional] 
**safety** | **str** |  | [optional] 
**attack_complexity** | **str** |  | [optional] 
**attack_requirements** | **str** |  | [optional] 
**attack_vector** | **str** |  | [optional] 
**availability_requirement** | **str** |  | [optional] 
**base_score** | **float** |  | [optional] 
**base_severity** | **str** |  | [optional] 
**confidentiality_requirement** | **str** |  | [optional] 
**exploit_maturity** | **str** |  | [optional] 
**integrity_requirement** | **str** |  | [optional] 
**modified_attack_complexity** | **str** |  | [optional] 
**modified_attack_requirements** | **str** |  | [optional] 
**modified_attack_vector** | **str** |  | [optional] 
**modified_privileges_required** | **str** |  | [optional] 
**modified_sub_availability_impact** | **str** |  | [optional] 
**modified_sub_confidentiality_impact** | **str** |  | [optional] 
**modified_sub_integrity_impact** | **str** |  | [optional] 
**modified_user_interaction** | **str** |  | [optional] 
**modified_vuln_availability_impact** | **str** |  | [optional] 
**modified_vuln_confidentiality_impact** | **str** |  | [optional] 
**modified_vuln_integrity_impact** | **str** |  | [optional] 
**privileges_required** | **str** |  | [optional] 
**provider_urgency** | **str** |  | [optional] 
**sub_availability_impact** | **str** |  | [optional] 
**sub_confidentiality_impact** | **str** |  | [optional] 
**sub_integrity_impact** | **str** |  | [optional] 
**user_interaction** | **str** |  | [optional] 
**value_density** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**vuln_availability_impact** | **str** |  | [optional] 
**vuln_confidentiality_impact** | **str** |  | [optional] 
**vuln_integrity_impact** | **str** |  | [optional] 
**vulnerability_response_effort** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvssv40 import AdvisoryCVSSV40

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVSSV40 from a JSON string
advisory_cvssv40_instance = AdvisoryCVSSV40.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVSSV40.to_json())

# convert the object into a dict
advisory_cvssv40_dict = advisory_cvssv40_instance.to_dict()
# create an instance of AdvisoryCVSSV40 from a dict
advisory_cvssv40_from_dict = AdvisoryCVSSV40.from_dict(advisory_cvssv40_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


