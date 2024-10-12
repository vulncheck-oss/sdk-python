# ApiCveItemsExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**configurations** | [**ApiConfigurations**](ApiConfigurations.md) |  | [optional] 
**cve** | [**ApiCVEExtended**](ApiCVEExtended.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**document_generation_date** | **str** | the deep tag instructs deep.Equal to ignore this field (used during OpenSearch loading) | [optional] 
**impact** | [**ApiImpactExtended**](ApiImpactExtended.md) |  | [optional] 
**last_modified_date** | **str** |  | [optional] 
**mitre_attack_techniques** | [**List[ApiMitreAttackTech]**](ApiMitreAttackTech.md) |  | [optional] 
**published_date** | **str** |  | [optional] 
**related_attack_patterns** | [**List[ApiRelatedAttackPattern]**](ApiRelatedAttackPattern.md) |  | [optional] 
**vc_configurations** | [**ApiConfigurations**](ApiConfigurations.md) |  | [optional] 
**vc_vulnerable_cpes** | **List[str]** |  | [optional] 
**vulnerable_cpes** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cve_items_extended import ApiCveItemsExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCveItemsExtended from a JSON string
api_cve_items_extended_instance = ApiCveItemsExtended.from_json(json)
# print the JSON string representation of the object
print(ApiCveItemsExtended.to_json())

# convert the object into a dict
api_cve_items_extended_dict = api_cve_items_extended_instance.to_dict()
# create an instance of ApiCveItemsExtended from a dict
api_cve_items_extended_from_dict = ApiCveItemsExtended.from_dict(api_cve_items_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


