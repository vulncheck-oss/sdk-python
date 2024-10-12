# ApiNVD20MetricExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_metric_v2** | [**List[ApiNVD20CvssMetricV2]**](ApiNVD20CvssMetricV2.md) |  | [optional] 
**cvss_metric_v30** | [**List[ApiNVD20CvssMetricV3]**](ApiNVD20CvssMetricV3.md) |  | [optional] 
**cvss_metric_v31** | [**List[ApiNVD20CvssMetricV3]**](ApiNVD20CvssMetricV3.md) |  | [optional] 
**cvss_metric_v40** | [**List[ApiNVD20CvssMetricV40]**](ApiNVD20CvssMetricV40.md) |  | [optional] 
**epss** | [**ApiEPSS**](ApiEPSS.md) |  | [optional] 
**temporal_cvssv2** | [**ApiNVD20TemporalCVSSV2**](ApiNVD20TemporalCVSSV2.md) |  | [optional] 
**temporal_cvssv2_secondary** | [**List[ApiNVD20TemporalCVSSV2]**](ApiNVD20TemporalCVSSV2.md) |  | [optional] 
**temporal_cvssv30** | [**ApiNVD20TemporalCVSSV3**](ApiNVD20TemporalCVSSV3.md) |  | [optional] 
**temporal_cvssv30_secondary** | [**List[ApiNVD20TemporalCVSSV3]**](ApiNVD20TemporalCVSSV3.md) |  | [optional] 
**temporal_cvssv31** | [**ApiNVD20TemporalCVSSV3**](ApiNVD20TemporalCVSSV3.md) |  | [optional] 
**temporal_cvssv31_secondary** | [**List[ApiNVD20TemporalCVSSV3]**](ApiNVD20TemporalCVSSV3.md) |  | [optional] 
**threat_cvssv40** | [**ApiNVD20ThreatCVSSV40**](ApiNVD20ThreatCVSSV40.md) |  | [optional] 
**threat_cvssv40_secondary** | [**List[ApiNVD20ThreatCVSSV40]**](ApiNVD20ThreatCVSSV40.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_metric_extended import ApiNVD20MetricExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20MetricExtended from a JSON string
api_nvd20_metric_extended_instance = ApiNVD20MetricExtended.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20MetricExtended.to_json())

# convert the object into a dict
api_nvd20_metric_extended_dict = api_nvd20_metric_extended_instance.to_dict()
# create an instance of ApiNVD20MetricExtended from a dict
api_nvd20_metric_extended_from_dict = ApiNVD20MetricExtended.from_dict(api_nvd20_metric_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


