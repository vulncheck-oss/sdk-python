# AdvisoryCNNVDEntryJSON


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bugtraq_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**modified_date** | **str** |  | [optional] 
**name_cn** | **str** |  | [optional] 
**published_date** | **str** |  | [optional] 
**severity_cn** | **str** |  | [optional] 
**severity_en** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vuln_description_cn** | **str** |  | [optional] 
**vuln_solution** | **str** |  | [optional] 
**vuln_type_cn** | **str** |  | [optional] 
**vuln_type_en** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cnnvd_entry_json import AdvisoryCNNVDEntryJSON

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCNNVDEntryJSON from a JSON string
advisory_cnnvd_entry_json_instance = AdvisoryCNNVDEntryJSON.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCNNVDEntryJSON.to_json())

# convert the object into a dict
advisory_cnnvd_entry_json_dict = advisory_cnnvd_entry_json_instance.to_dict()
# create an instance of AdvisoryCNNVDEntryJSON from a dict
advisory_cnnvd_entry_json_from_dict = AdvisoryCNNVDEntryJSON.from_dict(advisory_cnnvd_entry_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


