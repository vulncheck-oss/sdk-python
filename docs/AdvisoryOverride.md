# AdvisoryOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation** | [**AdvisoryOverrideAnnotation**](AdvisoryOverrideAnnotation.md) |  | [optional] 
**cve** | [**AdvisoryOverrideCVE**](AdvisoryOverrideCVE.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_override import AdvisoryOverride

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOverride from a JSON string
advisory_override_instance = AdvisoryOverride.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOverride.to_json())

# convert the object into a dict
advisory_override_dict = advisory_override_instance.to_dict()
# create an instance of AdvisoryOverride from a dict
advisory_override_from_dict = AdvisoryOverride.from_dict(advisory_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


