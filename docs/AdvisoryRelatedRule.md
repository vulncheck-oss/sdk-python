# AdvisoryRelatedRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_related_rule import AdvisoryRelatedRule

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRelatedRule from a JSON string
advisory_related_rule_instance = AdvisoryRelatedRule.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRelatedRule.to_json())

# convert the object into a dict
advisory_related_rule_dict = advisory_related_rule_instance.to_dict()
# create an instance of AdvisoryRelatedRule from a dict
advisory_related_rule_from_dict = AdvisoryRelatedRule.from_dict(advisory_related_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


