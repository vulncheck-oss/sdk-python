# ApiNVD20CVEExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**timestamp** | **str** | the deep tag instructs deep.Equal to ignore this field (used during OpenSearch loading) | [optional] 
**categorization** | [**ApiCategorizationExtended**](ApiCategorizationExtended.md) |  | [optional] 
**cisa_action_due** | **str** |  | [optional] 
**cisa_exploit_add** | **str** |  | [optional] 
**cisa_required_action** | **str** |  | [optional] 
**cisa_vulnerability_name** | **str** |  | [optional] 
**configurations** | [**List[AdvisoryNVD20Configuration]**](AdvisoryNVD20Configuration.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**descriptions** | [**List[ApiNVD20Description]**](ApiNVD20Description.md) |  | [optional] 
**document_generation_date** | **str** |  | [optional] 
**evaluator_comment** | **str** |  | [optional] 
**evaluator_impact** | **str** |  | [optional] 
**evaluator_solution** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**metrics** | [**ApiNVD20MetricExtended**](ApiNVD20MetricExtended.md) |  | [optional] 
**mitre_attack_techniques** | [**List[ApiMitreAttackTech]**](ApiMitreAttackTech.md) |  | [optional] 
**published** | **str** |  | [optional] 
**references** | [**List[ApiNVD20ReferenceExtended]**](ApiNVD20ReferenceExtended.md) |  | [optional] 
**related_attack_patterns** | [**List[ApiRelatedAttackPattern]**](ApiRelatedAttackPattern.md) |  | [optional] 
**source_identifier** | **str** |  | [optional] 
**vc_configurations** | [**List[AdvisoryNVD20Configuration]**](AdvisoryNVD20Configuration.md) |  | [optional] 
**vc_vulnerable_cpes** | **List[str]** |  | [optional] 
**vendor_comments** | [**List[ApiNVD20VendorComment]**](ApiNVD20VendorComment.md) |  | [optional] 
**vuln_status** | **str** |  | [optional] 
**vulncheck_kev_exploit_add** | **str** |  | [optional] 
**vulnerable_cpes** | **List[str]** |  | [optional] 
**weaknesses** | [**List[ApiNVD20WeaknessExtended]**](ApiNVD20WeaknessExtended.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_cve_extended import ApiNVD20CVEExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20CVEExtended from a JSON string
api_nvd20_cve_extended_instance = ApiNVD20CVEExtended.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20CVEExtended.to_json())

# convert the object into a dict
api_nvd20_cve_extended_dict = api_nvd20_cve_extended_instance.to_dict()
# create an instance of ApiNVD20CVEExtended from a dict
api_nvd20_cve_extended_from_dict = ApiNVD20CVEExtended.from_dict(api_nvd20_cve_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


