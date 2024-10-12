# AdvisoryMRemediation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_files** | [**List[AdvisoryAffectedFile]**](AdvisoryAffectedFile.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**date_specified** | **bool** |  | [optional] 
**description** | [**AdvisoryIVal**](AdvisoryIVal.md) |  | [optional] 
**fixed_build** | **str** |  | [optional] 
**product_id** | **List[str]** |  | [optional] 
**restart_required** | [**AdvisoryIVal**](AdvisoryIVal.md) |  | [optional] 
**sub_type** | **str** |  | [optional] 
**type** | **int** | diff | [optional] 
**url** | **str** |  | [optional] 
**supercedence** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_remediation import AdvisoryMRemediation

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMRemediation from a JSON string
advisory_m_remediation_instance = AdvisoryMRemediation.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMRemediation.to_json())

# convert the object into a dict
advisory_m_remediation_dict = advisory_m_remediation_instance.to_dict()
# create an instance of AdvisoryMRemediation from a dict
advisory_m_remediation_from_dict = AdvisoryMRemediation.from_dict(advisory_m_remediation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


