# AdvisoryBDUEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os** | [**AdvisoryBDUOs**](AdvisoryBDUOs.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bdu_environment import AdvisoryBDUEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUEnvironment from a JSON string
advisory_bdu_environment_instance = AdvisoryBDUEnvironment.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUEnvironment.to_json())

# convert the object into a dict
advisory_bdu_environment_dict = advisory_bdu_environment_instance.to_dict()
# create an instance of AdvisoryBDUEnvironment from a dict
advisory_bdu_environment_from_dict = AdvisoryBDUEnvironment.from_dict(advisory_bdu_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


