# ApiNVD20ThreatCVSSV40


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_base_metric_v40** | [**ApiNVD20ThreatAssociatedBaseMetric**](ApiNVD20ThreatAssociatedBaseMetric.md) |  | [optional] 
**base_threat_score** | **float** |  | [optional] 
**base_threat_severity** | **str** |  | [optional] 
**exploit_maturity** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_threat_cvssv40 import ApiNVD20ThreatCVSSV40

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20ThreatCVSSV40 from a JSON string
api_nvd20_threat_cvssv40_instance = ApiNVD20ThreatCVSSV40.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20ThreatCVSSV40.to_json())

# convert the object into a dict
api_nvd20_threat_cvssv40_dict = api_nvd20_threat_cvssv40_instance.to_dict()
# create an instance of ApiNVD20ThreatCVSSV40 from a dict
api_nvd20_threat_cvssv40_from_dict = ApiNVD20ThreatCVSSV40.from_dict(api_nvd20_threat_cvssv40_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


