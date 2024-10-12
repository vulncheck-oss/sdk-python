# AdvisoryRemediationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**entitlements** | **List[str]** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 
**product_ids** | **List[str]** |  | [optional] 
**restart_required** | [**AdvisoryRestartData**](AdvisoryRestartData.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_remediation_data import AdvisoryRemediationData

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRemediationData from a JSON string
advisory_remediation_data_instance = AdvisoryRemediationData.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRemediationData.to_json())

# convert the object into a dict
advisory_remediation_data_dict = advisory_remediation_data_instance.to_dict()
# create an instance of AdvisoryRemediationData from a dict
advisory_remediation_data_from_dict = AdvisoryRemediationData.from_dict(advisory_remediation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


