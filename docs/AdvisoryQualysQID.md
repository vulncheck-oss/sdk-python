# AdvisoryQualysQID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consequence** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_v2** | [**List[AdvisoryCvsssV23]**](AdvisoryCvsssV23.md) |  | [optional] 
**cvss_v3** | [**List[AdvisoryCvsssV23]**](AdvisoryCvsssV23.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_insert** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**patches** | [**List[AdvisoryPatch]**](AdvisoryPatch.md) |  | [optional] 
**published** | **str** |  | [optional] 
**qid** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor_refs** | [**List[AdvisoryVendorRef]**](AdvisoryVendorRef.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_qualys_qid import AdvisoryQualysQID

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryQualysQID from a JSON string
advisory_qualys_qid_instance = AdvisoryQualysQID.from_json(json)
# print the JSON string representation of the object
print(AdvisoryQualysQID.to_json())

# convert the object into a dict
advisory_qualys_qid_dict = advisory_qualys_qid_instance.to_dict()
# create an instance of AdvisoryQualysQID from a dict
advisory_qualys_qid_from_dict = AdvisoryQualysQID.from_dict(advisory_qualys_qid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


