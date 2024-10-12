# AdvisoryCvrf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**notes** | [**List[AdvisoryDocumentNote]**](AdvisoryDocumentNote.md) |  | [optional] 
**product_tree** | [**AdvisoryProductTree**](AdvisoryProductTree.md) |  | [optional] 
**references** | [**List[AdvisoryCVRFReference]**](AdvisoryCVRFReference.md) |  | [optional] 
**title** | **str** |  | [optional] 
**tracking** | [**AdvisoryDocumentTracking**](AdvisoryDocumentTracking.md) |  | [optional] 
**vulnerabilities** | [**List[AdvisoryVulnerability]**](AdvisoryVulnerability.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvrf import AdvisoryCvrf

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCvrf from a JSON string
advisory_cvrf_instance = AdvisoryCvrf.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCvrf.to_json())

# convert the object into a dict
advisory_cvrf_dict = advisory_cvrf_instance.to_dict()
# create an instance of AdvisoryCvrf from a dict
advisory_cvrf_from_dict = AdvisoryCvrf.from_dict(advisory_cvrf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


