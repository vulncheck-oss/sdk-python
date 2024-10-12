# ApiNVD20CvssDataV2


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
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cvss_data_v2 import ApiNVD20CvssDataV2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CvssDataV2 from a JSON string
api_nvd20_cvss_data_v2_instance = ApiNVD20CvssDataV2.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CvssDataV2.to_json())

# convert the object into a dict
api_nvd20_cvss_data_v2_dict = api_nvd20_cvss_data_v2_instance.to_dict()
# create an instance of ApiNVD20CvssDataV2 from a dict
api_nvd20_cvss_data_v2_from_dict = ApiNVD20CvssDataV2.from_dict(api_nvd20_cvss_data_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


