# AdvisoryVulnrichmentMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**other** | [**AdvisoryVulnrichmentOther**](AdvisoryVulnrichmentOther.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnrichment_metric import AdvisoryVulnrichmentMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnrichmentMetric from a JSON string
advisory_vulnrichment_metric_instance = AdvisoryVulnrichmentMetric.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnrichmentMetric.to_json())

# convert the object into a dict
advisory_vulnrichment_metric_dict = advisory_vulnrichment_metric_instance.to_dict()
# create an instance of AdvisoryVulnrichmentMetric from a dict
advisory_vulnrichment_metric_from_dict = AdvisoryVulnrichmentMetric.from_dict(advisory_vulnrichment_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


