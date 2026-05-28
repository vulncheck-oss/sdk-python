# AdvisoryOPCFoundationInvolvement

advisory.OPCFoundationInvolvement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_opc_foundation_involvement import AdvisoryOPCFoundationInvolvement

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOPCFoundationInvolvement from a JSON string
advisory_opc_foundation_involvement_instance = AdvisoryOPCFoundationInvolvement.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOPCFoundationInvolvement.to_json())

# convert the object into a dict
advisory_opc_foundation_involvement_dict = advisory_opc_foundation_involvement_instance.to_dict()
# create an instance of AdvisoryOPCFoundationInvolvement from a dict
advisory_opc_foundation_involvement_from_dict = AdvisoryOPCFoundationInvolvement.from_dict(advisory_opc_foundation_involvement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


