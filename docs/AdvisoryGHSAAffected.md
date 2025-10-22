# AdvisoryGHSAAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem_specific** | [**AdvisoryGHSAEcoSystemSpecific**](AdvisoryGHSAEcoSystemSpecific.md) |  | [optional] 
**package** | [**AdvisoryGHSAPackage**](AdvisoryGHSAPackage.md) |  | [optional] 
**ranges** | [**List[AdvisoryGHSARange]**](AdvisoryGHSARange.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ghsa_affected import AdvisoryGHSAAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHSAAffected from a JSON string
advisory_ghsa_affected_instance = AdvisoryGHSAAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHSAAffected.to_json())

# convert the object into a dict
advisory_ghsa_affected_dict = advisory_ghsa_affected_instance.to_dict()
# create an instance of AdvisoryGHSAAffected from a dict
advisory_ghsa_affected_from_dict = AdvisoryGHSAAffected.from_dict(advisory_ghsa_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


