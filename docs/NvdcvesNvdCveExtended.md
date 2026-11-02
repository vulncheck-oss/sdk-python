# NvdcvesNvdCveExtended

nvdcves.NvdCveExtended

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[ApiNVD20Affected]**](ApiNVD20Affected.md) |  | [optional] 
**cisa_action_due** | **str** |  | [optional] 
**cisa_exploit_add** | **str** |  | [optional] 
**cisa_required_action** | **str** |  | [optional] 
**cisa_vulnerability_name** | **str** |  | [optional] 
**configurations** | [**List[AdvisoryNVD20Configuration]**](AdvisoryNVD20Configuration.md) |  | [optional] 
**cve_tags** | [**List[ApiNVD20CVETag]**](ApiNVD20CVETag.md) |  | [optional] 
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
**vc_configurations_with_platforms** | [**List[AdvisoryNVD20Configuration]**](AdvisoryNVD20Configuration.md) | VCConfigurationsWithPlatforms is VCConfigurations with NVD-style platform (\&quot;running on\&quot;) nodes: a configuration whose product needs a platform is AND{the vulnerable node, a node of vulnerable:false platform CPEs}. Only set when at least one configuration has a platform. | [optional] 
**vc_vulnerable_cpes** | **List[str]** |  | [optional] 
**vendor_comments** | [**List[ApiNVD20VendorComment]**](ApiNVD20VendorComment.md) |  | [optional] 
**vuln_status** | **str** |  | [optional] 
**weaknesses** | [**List[ApiNVD20Weakness]**](ApiNVD20Weakness.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.nvdcves_nvd_cve_extended import NvdcvesNvdCveExtended

# TODO update the JSON string below
json = "{}"
# create an instance of NvdcvesNvdCveExtended from a JSON string
nvdcves_nvd_cve_extended_instance = NvdcvesNvdCveExtended.from_json(json)
# print the JSON string representation of the object
print(NvdcvesNvdCveExtended.to_json())

# convert the object into a dict
nvdcves_nvd_cve_extended_dict = nvdcves_nvd_cve_extended_instance.to_dict()
# create an instance of NvdcvesNvdCveExtended from a dict
nvdcves_nvd_cve_extended_from_dict = NvdcvesNvdCveExtended.from_dict(nvdcves_nvd_cve_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


