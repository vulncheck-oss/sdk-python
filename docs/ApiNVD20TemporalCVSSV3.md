# ApiNVD20TemporalCVSSV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_base_metric_v3** | [**ApiNVD20TemporalAssociatedBaseMetric**](ApiNVD20TemporalAssociatedBaseMetric.md) |  | [optional] 
**exploit_code_maturity** | **str** |  | [optional] 
**remediation_level** | **str** |  | [optional] 
**report_confidence** | **str** |  | [optional] 
**temporal_score** | **float** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_temporal_cvssv3 import ApiNVD20TemporalCVSSV3

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20TemporalCVSSV3 from a JSON string
api_nvd20_temporal_cvssv3_instance = ApiNVD20TemporalCVSSV3.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20TemporalCVSSV3.to_json())

# convert the object into a dict
api_nvd20_temporal_cvssv3_dict = api_nvd20_temporal_cvssv3_instance.to_dict()
# create an instance of ApiNVD20TemporalCVSSV3 from a dict
api_nvd20_temporal_cvssv3_from_dict = ApiNVD20TemporalCVSSV3.from_dict(api_nvd20_temporal_cvssv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


