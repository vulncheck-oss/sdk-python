# AdvisoryOPCFoundationAdvisory

advisory.OPCFoundationAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf** | [**AdvisoryOPCFoundationRef**](AdvisoryOPCFoundationRef.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**gcve** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_opc_foundation_advisory import AdvisoryOPCFoundationAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOPCFoundationAdvisory from a JSON string
advisory_opc_foundation_advisory_instance = AdvisoryOPCFoundationAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOPCFoundationAdvisory.to_json())

# convert the object into a dict
advisory_opc_foundation_advisory_dict = advisory_opc_foundation_advisory_instance.to_dict()
# create an instance of AdvisoryOPCFoundationAdvisory from a dict
advisory_opc_foundation_advisory_from_dict = AdvisoryOPCFoundationAdvisory.from_dict(advisory_opc_foundation_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


