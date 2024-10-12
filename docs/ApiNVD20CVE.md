# ApiNVD20CVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cisa_action_due** | **str** |  | [optional] 
**cisa_exploit_add** | **str** |  | [optional] 
**cisa_required_action** | **str** |  | [optional] 
**cisa_vulnerability_name** | **str** |  | [optional] 
**configurations** | [**List[AdvisoryNVD20Configuration]**](AdvisoryNVD20Configuration.md) |  | [optional] 
**descriptions** | [**List[ApiNVD20Description]**](ApiNVD20Description.md) |  | [optional] 
**evaluator_comment** | **str** |  | [optional] 
**evaluator_impact** | **str** |  | [optional] 
**evaluator_solution** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**metrics** | [**ApiNVD20Metric**](ApiNVD20Metric.md) |  | [optional] 
**published** | **str** |  | [optional] 
**references** | [**List[ApiNVD20Reference]**](ApiNVD20Reference.md) |  | [optional] 
**source_identifier** | **str** |  | [optional] 
**vc_configurations** | [**List[AdvisoryNVD20Configuration]**](AdvisoryNVD20Configuration.md) |  | [optional] 
**vc_vulnerable_cpes** | **List[str]** |  | [optional] 
**vendor_comments** | [**List[ApiNVD20VendorComment]**](ApiNVD20VendorComment.md) |  | [optional] 
**vuln_status** | **str** |  | [optional] 
**weaknesses** | [**List[ApiNVD20Weakness]**](ApiNVD20Weakness.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cve import ApiNVD20CVE

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CVE from a JSON string
api_nvd20_cve_instance = ApiNVD20CVE.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CVE.to_json())

# convert the object into a dict
api_nvd20_cve_dict = api_nvd20_cve_instance.to_dict()
# create an instance of ApiNVD20CVE from a dict
api_nvd20_cve_from_dict = ApiNVD20CVE.from_dict(api_nvd20_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


