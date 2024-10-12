# AdvisoryMSCVRF


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_title** | [**AdvisoryMSDocumentTitle**](AdvisoryMSDocumentTitle.md) |  | [optional] 
**document_tracking** | [**AdvisoryMDocumentTracking**](AdvisoryMDocumentTracking.md) |  | [optional] 
**product_tree** | [**AdvisoryMProductTree**](AdvisoryMProductTree.md) |  | [optional] 
**document_type** | **str** |  | [optional] 
**documentnotes** | [**List[AdvisoryRNote]**](AdvisoryRNote.md) | diff | [optional] 
**documentpublisher** | [**AdvisoryDocumentPublisher**](AdvisoryDocumentPublisher.md) |  | [optional] 
**vulnerability** | [**List[AdvisoryMVulnerability]**](AdvisoryMVulnerability.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mscvrf import AdvisoryMSCVRF

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMSCVRF from a JSON string
advisory_mscvrf_instance = AdvisoryMSCVRF.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMSCVRF.to_json())

# convert the object into a dict
advisory_mscvrf_dict = advisory_mscvrf_instance.to_dict()
# create an instance of AdvisoryMSCVRF from a dict
advisory_mscvrf_from_dict = AdvisoryMSCVRF.from_dict(advisory_mscvrf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


