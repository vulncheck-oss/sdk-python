# ApiNVD20CvssMetricV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_data** | [**ApiNVD20CvssDataV3**](ApiNVD20CvssDataV3.md) |  | [optional] 
**exploitability_score** | **float** |  | [optional] 
**impact_score** | **float** |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cvss_metric_v3 import ApiNVD20CvssMetricV3

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CvssMetricV3 from a JSON string
api_nvd20_cvss_metric_v3_instance = ApiNVD20CvssMetricV3.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CvssMetricV3.to_json())

# convert the object into a dict
api_nvd20_cvss_metric_v3_dict = api_nvd20_cvss_metric_v3_instance.to_dict()
# create an instance of ApiNVD20CvssMetricV3 from a dict
api_nvd20_cvss_metric_v3_from_dict = ApiNVD20CvssMetricV3.from_dict(api_nvd20_cvss_metric_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


