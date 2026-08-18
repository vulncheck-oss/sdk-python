# ApiNVD20SsvcMetricV203

api.NVD20SsvcMetricV203

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**ssvc_data** | [**ApiNVD20SsvcDataV203**](ApiNVD20SsvcDataV203.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_ssvc_metric_v203 import ApiNVD20SsvcMetricV203

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20SsvcMetricV203 from a JSON string
api_nvd20_ssvc_metric_v203_instance = ApiNVD20SsvcMetricV203.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20SsvcMetricV203.to_json())

# convert the object into a dict
api_nvd20_ssvc_metric_v203_dict = api_nvd20_ssvc_metric_v203_instance.to_dict()
# create an instance of ApiNVD20SsvcMetricV203 from a dict
api_nvd20_ssvc_metric_v203_from_dict = ApiNVD20SsvcMetricV203.from_dict(api_nvd20_ssvc_metric_v203_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


