# ApiNVD20CvssMetricV40


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_data** | [**AdvisoryCVSSV40**](AdvisoryCVSSV40.md) |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cvss_metric_v40 import ApiNVD20CvssMetricV40

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CvssMetricV40 from a JSON string
api_nvd20_cvss_metric_v40_instance = ApiNVD20CvssMetricV40.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CvssMetricV40.to_json())

# convert the object into a dict
api_nvd20_cvss_metric_v40_dict = api_nvd20_cvss_metric_v40_instance.to_dict()
# create an instance of ApiNVD20CvssMetricV40 from a dict
api_nvd20_cvss_metric_v40_from_dict = ApiNVD20CvssMetricV40.from_dict(api_nvd20_cvss_metric_v40_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


