# AdvisoryMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_v2_0** | [**AdvisoryMCvssV20**](AdvisoryMCvssV20.md) |  | [optional] 
**cvss_v3_0** | [**AdvisoryMCvssV30**](AdvisoryMCvssV30.md) |  | [optional] 
**cvss_v3_1** | [**AdvisoryMCvssV31**](AdvisoryMCvssV31.md) |  | [optional] 
**cvss_v4_0** | [**AdvisoryMCvssV40**](AdvisoryMCvssV40.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_metric import AdvisoryMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMetric from a JSON string
advisory_metric_instance = AdvisoryMetric.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMetric.to_json())

# convert the object into a dict
advisory_metric_dict = advisory_metric_instance.to_dict()
# create an instance of AdvisoryMetric from a dict
advisory_metric_from_dict = AdvisoryMetric.from_dict(advisory_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


