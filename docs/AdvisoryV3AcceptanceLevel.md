# AdvisoryV3AcceptanceLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_v3_acceptance_level import AdvisoryV3AcceptanceLevel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryV3AcceptanceLevel from a JSON string
advisory_v3_acceptance_level_instance = AdvisoryV3AcceptanceLevel.from_json(json)
# print the JSON string representation of the object
print(AdvisoryV3AcceptanceLevel.to_json())

# convert the object into a dict
advisory_v3_acceptance_level_dict = advisory_v3_acceptance_level_instance.to_dict()
# create an instance of AdvisoryV3AcceptanceLevel from a dict
advisory_v3_acceptance_level_from_dict = AdvisoryV3AcceptanceLevel.from_dict(advisory_v3_acceptance_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


