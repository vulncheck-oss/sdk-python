# ApiNVD20CvssDataV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_complexity** | **str** |  | [optional] 
**attack_vector** | **str** |  | [optional] 
**availability_impact** | **str** |  | [optional] 
**availability_requirement** | **str** |  | [optional] 
**base_score** | **float** |  | [optional] 
**base_severity** | **str** |  | [optional] 
**confidentiality_impact** | **str** |  | [optional] 
**confidentiality_requirement** | **str** |  | [optional] 
**environmental_score** | **float** |  | [optional] 
**environmental_severity** | **str** |  | [optional] 
**exploit_code_maturity** | **str** |  | [optional] 
**integrity_impact** | **str** |  | [optional] 
**integrity_requirement** | **str** |  | [optional] 
**modified_attack_complexity** | **str** |  | [optional] 
**modified_attack_vector** | **str** |  | [optional] 
**modified_availability_impact** | **str** |  | [optional] 
**modified_confidentiality_impact** | **str** |  | [optional] 
**modified_integrity_impact** | **str** |  | [optional] 
**modified_privileges_required** | **str** |  | [optional] 
**modified_scope** | **str** |  | [optional] 
**modified_user_interaction** | **str** |  | [optional] 
**privileges_required** | **str** |  | [optional] 
**remediation_level** | **str** |  | [optional] 
**report_confidence** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**temporal_score** | **float** |  | [optional] 
**temporal_severity** | **str** |  | [optional] 
**user_interaction** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cvss_data_v3 import ApiNVD20CvssDataV3

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CvssDataV3 from a JSON string
api_nvd20_cvss_data_v3_instance = ApiNVD20CvssDataV3.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CvssDataV3.to_json())

# convert the object into a dict
api_nvd20_cvss_data_v3_dict = api_nvd20_cvss_data_v3_instance.to_dict()
# create an instance of ApiNVD20CvssDataV3 from a dict
api_nvd20_cvss_data_v3_from_dict = ApiNVD20CvssDataV3.from_dict(api_nvd20_cvss_data_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


