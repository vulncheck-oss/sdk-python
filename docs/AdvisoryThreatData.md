# AdvisoryThreatData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**product_ids** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_threat_data import AdvisoryThreatData

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryThreatData from a JSON string
advisory_threat_data_instance = AdvisoryThreatData.from_json(json)
# print the JSON string representation of the object
print(AdvisoryThreatData.to_json())

# convert the object into a dict
advisory_threat_data_dict = advisory_threat_data_instance.to_dict()
# create an instance of AdvisoryThreatData from a dict
advisory_threat_data_from_dict = AdvisoryThreatData.from_dict(advisory_threat_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


