# AdvisoryOverrideCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurations** | [**List[AdvisoryOverrideConfiguration]**](AdvisoryOverrideConfiguration.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_override_cve import AdvisoryOverrideCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOverrideCVE from a JSON string
advisory_override_cve_instance = AdvisoryOverrideCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOverrideCVE.to_json())

# convert the object into a dict
advisory_override_cve_dict = advisory_override_cve_instance.to_dict()
# create an instance of AdvisoryOverrideCVE from a dict
advisory_override_cve_from_dict = AdvisoryOverrideCVE.from_dict(advisory_override_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


