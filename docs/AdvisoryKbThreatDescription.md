# AdvisoryKbThreatDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dos** | **str** |  | [optional] 
**exploited** | **str** |  | [optional] 
**latest_software_release** | **str** |  | [optional] 
**level** | **List[str]** |  | [optional] 
**older_software_release** | **str** |  | [optional] 
**publicly_disclosed** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_kb_threat_description import AdvisoryKbThreatDescription

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryKbThreatDescription from a JSON string
advisory_kb_threat_description_instance = AdvisoryKbThreatDescription.from_json(json)
# print the JSON string representation of the object
print(AdvisoryKbThreatDescription.to_json())

# convert the object into a dict
advisory_kb_threat_description_dict = advisory_kb_threat_description_instance.to_dict()
# create an instance of AdvisoryKbThreatDescription from a dict
advisory_kb_threat_description_from_dict = AdvisoryKbThreatDescription.from_dict(advisory_kb_threat_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


