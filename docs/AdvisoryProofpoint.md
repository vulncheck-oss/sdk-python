# AdvisoryProofpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_proofpoint import AdvisoryProofpoint

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryProofpoint from a JSON string
advisory_proofpoint_instance = AdvisoryProofpoint.from_json(json)
# print the JSON string representation of the object
print(AdvisoryProofpoint.to_json())

# convert the object into a dict
advisory_proofpoint_dict = advisory_proofpoint_instance.to_dict()
# create an instance of AdvisoryProofpoint from a dict
advisory_proofpoint_from_dict = AdvisoryProofpoint.from_dict(advisory_proofpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


