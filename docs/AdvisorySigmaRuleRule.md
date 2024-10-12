# AdvisorySigmaRuleRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**detection** | **Dict[str, object]** |  | [optional] 
**false_positives** | **List[str]** |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**logsource** | [**AdvisoryLogSource**](AdvisoryLogSource.md) |  | [optional] 
**modified** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**related** | [**List[AdvisoryRelatedRule]**](AdvisoryRelatedRule.md) |  | [optional] 
**status** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sigma_rule_rule import AdvisorySigmaRuleRule

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySigmaRuleRule from a JSON string
advisory_sigma_rule_rule_instance = AdvisorySigmaRuleRule.from_json(json)
# print the JSON string representation of the object
print(AdvisorySigmaRuleRule.to_json())

# convert the object into a dict
advisory_sigma_rule_rule_dict = advisory_sigma_rule_rule_instance.to_dict()
# create an instance of AdvisorySigmaRuleRule from a dict
advisory_sigma_rule_rule_from_dict = AdvisorySigmaRuleRule.from_dict(advisory_sigma_rule_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


