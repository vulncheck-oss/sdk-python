# AdvisoryOPCFoundationRef

advisory.OPCFoundationRef

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**AdvisoryOPCFoundationDocumentMetadata**](AdvisoryOPCFoundationDocumentMetadata.md) |  | [optional] 
**product_tree** | [**AdvisoryProductBranch**](AdvisoryProductBranch.md) |  | [optional] 
**vulnerabilities** | [**List[AdvisoryOPCFoundationVulnerability]**](AdvisoryOPCFoundationVulnerability.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_opc_foundation_ref import AdvisoryOPCFoundationRef

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOPCFoundationRef from a JSON string
advisory_opc_foundation_ref_instance = AdvisoryOPCFoundationRef.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOPCFoundationRef.to_json())

# convert the object into a dict
advisory_opc_foundation_ref_dict = advisory_opc_foundation_ref_instance.to_dict()
# create an instance of AdvisoryOPCFoundationRef from a dict
advisory_opc_foundation_ref_from_dict = AdvisoryOPCFoundationRef.from_dict(advisory_opc_foundation_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


