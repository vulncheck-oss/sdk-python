# AdvisoryCNVDFlaw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products_cn** | **str** |  | [optional] 
**bugtraq_id** | **str** |  | [optional] 
**cnvd** | **str** |  | [optional] 
**collection_time** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**harm_level** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**public_date** | **str** |  | [optional] 
**reference_urls** | **List[str]** |  | [optional] 
**submission_time** | **str** |  | [optional] 
**title_cn** | **str** |  | [optional] 
**update_time** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**validation_info_cn** | **str** |  | [optional] 
**validation_info_en** | **str** |  | [optional] 
**vendor_patch_cn** | **str** |  | [optional] 
**vuln_attachments** | **List[str]** |  | [optional] 
**vuln_description_cn** | **str** |  | [optional] 
**vuln_solution_cn** | **str** |  | [optional] 
**vuln_type_cn** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cnvd_flaw import AdvisoryCNVDFlaw

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCNVDFlaw from a JSON string
advisory_cnvd_flaw_instance = AdvisoryCNVDFlaw.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCNVDFlaw.to_json())

# convert the object into a dict
advisory_cnvd_flaw_dict = advisory_cnvd_flaw_instance.to_dict()
# create an instance of AdvisoryCNVDFlaw from a dict
advisory_cnvd_flaw_from_dict = AdvisoryCNVDFlaw.from_dict(advisory_cnvd_flaw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


