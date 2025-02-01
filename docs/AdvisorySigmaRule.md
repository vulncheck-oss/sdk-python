# AdvisorySigmaRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**mitre_attack_techniques** | **List[str]** |  | [optional] 
**sigma_rule** | [**AdvisorySigmaRuleRule**](AdvisorySigmaRuleRule.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sigma_rule import AdvisorySigmaRule

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySigmaRule from a JSON string
advisory_sigma_rule_instance = AdvisorySigmaRule.from_json(json)
# print the JSON string representation of the object
print(AdvisorySigmaRule.to_json())

# convert the object into a dict
advisory_sigma_rule_dict = advisory_sigma_rule_instance.to_dict()
# create an instance of AdvisorySigmaRule from a dict
advisory_sigma_rule_from_dict = AdvisorySigmaRule.from_dict(advisory_sigma_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


