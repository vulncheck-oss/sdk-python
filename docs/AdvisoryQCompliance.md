# AdvisoryQCompliance

advisory.QCompliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | **str** |  | [optional] 
**typ** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_q_compliance import AdvisoryQCompliance

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryQCompliance from a JSON string
advisory_q_compliance_instance = AdvisoryQCompliance.from_json(json)
# print the JSON string representation of the object
print(AdvisoryQCompliance.to_json())

# convert the object into a dict
advisory_q_compliance_dict = advisory_q_compliance_instance.to_dict()
# create an instance of AdvisoryQCompliance from a dict
advisory_q_compliance_from_dict = AdvisoryQCompliance.from_dict(advisory_q_compliance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


