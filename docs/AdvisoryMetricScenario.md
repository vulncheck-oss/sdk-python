# AdvisoryMetricScenario


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_metric_scenario import AdvisoryMetricScenario

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMetricScenario from a JSON string
advisory_metric_scenario_instance = AdvisoryMetricScenario.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMetricScenario.to_json())

# convert the object into a dict
advisory_metric_scenario_dict = advisory_metric_scenario_instance.to_dict()
# create an instance of AdvisoryMetricScenario from a dict
advisory_metric_scenario_from_dict = AdvisoryMetricScenario.from_dict(advisory_metric_scenario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


