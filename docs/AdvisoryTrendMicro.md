# AdvisoryTrendMicro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**scores** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_trend_micro import AdvisoryTrendMicro

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTrendMicro from a JSON string
advisory_trend_micro_instance = AdvisoryTrendMicro.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTrendMicro.to_json())

# convert the object into a dict
advisory_trend_micro_dict = advisory_trend_micro_instance.to_dict()
# create an instance of AdvisoryTrendMicro from a dict
advisory_trend_micro_from_dict = AdvisoryTrendMicro.from_dict(advisory_trend_micro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


