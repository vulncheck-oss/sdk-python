# AdvisoryMicrosoftKb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**kbs** | [**List[AdvisoryKb]**](AdvisoryKb.md) |  | [optional] 
**threat** | [**AdvisoryKbThreatDescription**](AdvisoryKbThreatDescription.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_microsoft_kb import AdvisoryMicrosoftKb

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMicrosoftKb from a JSON string
advisory_microsoft_kb_instance = AdvisoryMicrosoftKb.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMicrosoftKb.to_json())

# convert the object into a dict
advisory_microsoft_kb_dict = advisory_microsoft_kb_instance.to_dict()
# create an instance of AdvisoryMicrosoftKb from a dict
advisory_microsoft_kb_from_dict = AdvisoryMicrosoftKb.from_dict(advisory_microsoft_kb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


