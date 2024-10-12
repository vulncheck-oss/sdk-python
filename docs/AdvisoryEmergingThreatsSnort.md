# AdvisoryEmergingThreatsSnort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**rev** | **str** |  | [optional] 
**rule_disabled** | **bool** |  | [optional] 
**rule_name** | **str** |  | [optional] 
**sid** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_emerging_threats_snort import AdvisoryEmergingThreatsSnort

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEmergingThreatsSnort from a JSON string
advisory_emerging_threats_snort_instance = AdvisoryEmergingThreatsSnort.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEmergingThreatsSnort.to_json())

# convert the object into a dict
advisory_emerging_threats_snort_dict = advisory_emerging_threats_snort_instance.to_dict()
# create an instance of AdvisoryEmergingThreatsSnort from a dict
advisory_emerging_threats_snort_from_dict = AdvisoryEmergingThreatsSnort.from_dict(advisory_emerging_threats_snort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


