# AdvisoryJetBrains


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cwe** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**resolved_in** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_jet_brains import AdvisoryJetBrains

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJetBrains from a JSON string
advisory_jet_brains_instance = AdvisoryJetBrains.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJetBrains.to_json())

# convert the object into a dict
advisory_jet_brains_dict = advisory_jet_brains_instance.to_dict()
# create an instance of AdvisoryJetBrains from a dict
advisory_jet_brains_from_dict = AdvisoryJetBrains.from_dict(advisory_jet_brains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


