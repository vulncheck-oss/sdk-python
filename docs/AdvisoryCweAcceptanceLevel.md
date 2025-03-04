# AdvisoryCweAcceptanceLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cwe_acceptance_level import AdvisoryCweAcceptanceLevel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCweAcceptanceLevel from a JSON string
advisory_cwe_acceptance_level_instance = AdvisoryCweAcceptanceLevel.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCweAcceptanceLevel.to_json())

# convert the object into a dict
advisory_cwe_acceptance_level_dict = advisory_cwe_acceptance_level_instance.to_dict()
# create an instance of AdvisoryCweAcceptanceLevel from a dict
advisory_cwe_acceptance_level_from_dict = AdvisoryCweAcceptanceLevel.from_dict(advisory_cwe_acceptance_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


