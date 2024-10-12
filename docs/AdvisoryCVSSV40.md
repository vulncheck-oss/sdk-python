# AdvisoryCVSSV40


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_complexity** | **str** |  | [optional] 
**attack_requirements** | **str** |  | [optional] 
**attack_vector** | **str** |  | [optional] 
**automatable** | **str** | mod NVD | [optional] 
**availability_requirements** | **str** | mod NVD | [optional] 
**base_score** | **float** |  | [optional] 
**base_severity** | **str** |  | [optional] 
**confidentiality_requirements** | **str** | mod NVD | [optional] 
**exploit_maturity** | **str** |  | [optional] 
**integrity_requirements** | **str** | mod NVD | [optional] 
**modified_attack_complexity** | **str** |  | [optional] 
**modified_attack_requirements** | **str** |  | [optional] 
**modified_attack_vector** | **str** |  | [optional] 
**modified_privileges_required** | **str** |  | [optional] 
**modified_subsequent_system_availability** | **str** | mod NVD | [optional] 
**modified_subsequent_system_confidentiality** | **str** | mod NVD | [optional] 
**modified_subsequent_system_integrity** | **str** | mod NVD | [optional] 
**modified_user_interaction** | **str** |  | [optional] 
**modified_vulnerable_system_availability** | **str** | mod NVD | [optional] 
**modified_vulnerable_system_confidentiality** | **str** | mod NVD | [optional] 
**modified_vulnerable_system_integrity** | **str** | mod NVD | [optional] 
**privileges_required** | **str** |  | [optional] 
**provider_urgency** | **str** |  | [optional] 
**recovery** | **str** | mod NVD | [optional] 
**safety** | **str** | mod NVD | [optional] 
**subsequent_system_availability** | **str** | mod NVD | [optional] 
**subsequent_system_confidentiality** | **str** | mod NVD | [optional] 
**subsequent_system_integrity** | **str** | mod NVD | [optional] 
**user_interaction** | **str** |  | [optional] 
**value_density** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**vulnerability_response_effort** | **str** |  | [optional] 
**vulnerable_system_availability** | **str** | mod NVD | [optional] 
**vulnerable_system_confidentiality** | **str** | mod NVD | [optional] 
**vulnerable_system_integrity** | **str** | mod NVD | [optional] 

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


