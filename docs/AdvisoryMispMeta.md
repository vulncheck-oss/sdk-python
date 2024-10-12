# AdvisoryMispMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_confidence** | **str** |  | [optional] 
**cfr_suspected_state_sponsor** | **str** |  | [optional] 
**cfr_suspected_victims** | **List[str]** |  | [optional] 
**cfr_target_category** | **List[str]** |  | [optional] 
**cfr_type_of_incident** | **List[str]** |  | [optional] 
**country** | **str** |  | [optional] 
**refs** | **List[str]** |  | [optional] 
**synonyms** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_misp_meta import AdvisoryMispMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMispMeta from a JSON string
advisory_misp_meta_instance = AdvisoryMispMeta.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMispMeta.to_json())

# convert the object into a dict
advisory_misp_meta_dict = advisory_misp_meta_instance.to_dict()
# create an instance of AdvisoryMispMeta from a dict
advisory_misp_meta_from_dict = AdvisoryMispMeta.from_dict(advisory_misp_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


