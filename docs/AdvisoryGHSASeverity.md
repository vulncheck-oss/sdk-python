# AdvisoryGHSASeverity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ghsa_severity import AdvisoryGHSASeverity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHSASeverity from a JSON string
advisory_ghsa_severity_instance = AdvisoryGHSASeverity.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHSASeverity.to_json())

# convert the object into a dict
advisory_ghsa_severity_dict = advisory_ghsa_severity_instance.to_dict()
# create an instance of AdvisoryGHSASeverity from a dict
advisory_ghsa_severity_from_dict = AdvisoryGHSASeverity.from_dict(advisory_ghsa_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


