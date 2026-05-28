# AdvisoryOPCFoundationAcknowledgment

advisory.OPCFoundationAcknowledgment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** |  | [optional] 
**organization** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_opc_foundation_acknowledgment import AdvisoryOPCFoundationAcknowledgment

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOPCFoundationAcknowledgment from a JSON string
advisory_opc_foundation_acknowledgment_instance = AdvisoryOPCFoundationAcknowledgment.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOPCFoundationAcknowledgment.to_json())

# convert the object into a dict
advisory_opc_foundation_acknowledgment_dict = advisory_opc_foundation_acknowledgment_instance.to_dict()
# create an instance of AdvisoryOPCFoundationAcknowledgment from a dict
advisory_opc_foundation_acknowledgment_from_dict = AdvisoryOPCFoundationAcknowledgment.from_dict(advisory_opc_foundation_acknowledgment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


