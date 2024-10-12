# AdvisorySeverity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_severity import AdvisorySeverity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySeverity from a JSON string
advisory_severity_instance = AdvisorySeverity.from_json(json)
# print the JSON string representation of the object
print(AdvisorySeverity.to_json())

# convert the object into a dict
advisory_severity_dict = advisory_severity_instance.to_dict()
# create an instance of AdvisorySeverity from a dict
advisory_severity_from_dict = AdvisorySeverity.from_dict(advisory_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


