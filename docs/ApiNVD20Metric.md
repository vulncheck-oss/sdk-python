# ApiNVD20Metric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_metric_v2** | [**List[ApiNVD20CvssMetricV2]**](ApiNVD20CvssMetricV2.md) |  | [optional] 
**cvss_metric_v30** | [**List[ApiNVD20CvssMetricV3]**](ApiNVD20CvssMetricV3.md) |  | [optional] 
**cvss_metric_v31** | [**List[ApiNVD20CvssMetricV3]**](ApiNVD20CvssMetricV3.md) |  | [optional] 
**cvss_metric_v40** | [**List[ApiNVD20CvssMetricV40]**](ApiNVD20CvssMetricV40.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_metric import ApiNVD20Metric

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20Metric from a JSON string
api_nvd20_metric_instance = ApiNVD20Metric.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20Metric.to_json())

# convert the object into a dict
api_nvd20_metric_dict = api_nvd20_metric_instance.to_dict()
# create an instance of ApiNVD20Metric from a dict
api_nvd20_metric_from_dict = ApiNVD20Metric.from_dict(api_nvd20_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


