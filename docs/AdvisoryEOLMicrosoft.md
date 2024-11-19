# AdvisoryEOLMicrosoft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**edition** | **str** |  | [optional] 
**extended_end_date** | **str** |  | [optional] 
**mainstream_date** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**release** | **str** |  | [optional] 
**release_end_date** | **str** |  | [optional] 
**release_start_date** | **str** |  | [optional] 
**retirement_date** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**support_policy** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_eol_microsoft import AdvisoryEOLMicrosoft

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEOLMicrosoft from a JSON string
advisory_eol_microsoft_instance = AdvisoryEOLMicrosoft.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEOLMicrosoft.to_json())

# convert the object into a dict
advisory_eol_microsoft_dict = advisory_eol_microsoft_instance.to_dict()
# create an instance of AdvisoryEOLMicrosoft from a dict
advisory_eol_microsoft_from_dict = AdvisoryEOLMicrosoft.from_dict(advisory_eol_microsoft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


