# AdvisoryOverrideConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[AdvisoryCPENode]**](AdvisoryCPENode.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_override_configuration import AdvisoryOverrideConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOverrideConfiguration from a JSON string
advisory_override_configuration_instance = AdvisoryOverrideConfiguration.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOverrideConfiguration.to_json())

# convert the object into a dict
advisory_override_configuration_dict = advisory_override_configuration_instance.to_dict()
# create an instance of AdvisoryOverrideConfiguration from a dict
advisory_override_configuration_from_dict = AdvisoryOverrideConfiguration.from_dict(advisory_override_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


