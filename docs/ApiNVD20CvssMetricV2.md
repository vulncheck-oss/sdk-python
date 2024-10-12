# ApiNVD20CvssMetricV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ac_insuf_info** | **bool** |  | [optional] 
**base_severity** | **str** |  | [optional] 
**cvss_data** | [**ApiNVD20CvssDataV2**](ApiNVD20CvssDataV2.md) |  | [optional] 
**exploitability_score** | **float** |  | [optional] 
**impact_score** | **float** |  | [optional] 
**obtain_all_privilege** | **bool** |  | [optional] 
**obtain_other_privilege** | **bool** |  | [optional] 
**obtain_user_privilege** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**user_interaction_required** | **bool** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cvss_metric_v2 import ApiNVD20CvssMetricV2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CvssMetricV2 from a JSON string
api_nvd20_cvss_metric_v2_instance = ApiNVD20CvssMetricV2.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CvssMetricV2.to_json())

# convert the object into a dict
api_nvd20_cvss_metric_v2_dict = api_nvd20_cvss_metric_v2_instance.to_dict()
# create an instance of ApiNVD20CvssMetricV2 from a dict
api_nvd20_cvss_metric_v2_from_dict = ApiNVD20CvssMetricV2.from_dict(api_nvd20_cvss_metric_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


