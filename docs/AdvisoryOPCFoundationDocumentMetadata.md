# AdvisoryOPCFoundationDocumentMetadata

advisory.OPCFoundationDocumentMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**csaf_version** | **str** |  | [optional] 
**distribution** | [**AdvisoryOPCFoundationDistribution**](AdvisoryOPCFoundationDistribution.md) |  | [optional] 
**lang** | **str** |  | [optional] 
**notes** | [**List[AdvisoryCSAFNote]**](AdvisoryCSAFNote.md) | used by ncsc | [optional] 
**publisher** | [**AdvisoryPublisher**](AdvisoryPublisher.md) |  | [optional] 
**references** | [**List[AdvisoryCSAFReference]**](AdvisoryCSAFReference.md) |  | [optional] 
**title** | **str** | Aggregate severity is a vehicle that is provided by the document producer to convey the urgency and criticality with which the one or more vulnerabilities reported should be addressed. | [optional] 
**tracking** | [**AdvisoryTracking**](AdvisoryTracking.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_opc_foundation_document_metadata import AdvisoryOPCFoundationDocumentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOPCFoundationDocumentMetadata from a JSON string
advisory_opc_foundation_document_metadata_instance = AdvisoryOPCFoundationDocumentMetadata.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOPCFoundationDocumentMetadata.to_json())

# convert the object into a dict
advisory_opc_foundation_document_metadata_dict = advisory_opc_foundation_document_metadata_instance.to_dict()
# create an instance of AdvisoryOPCFoundationDocumentMetadata from a dict
advisory_opc_foundation_document_metadata_from_dict = AdvisoryOPCFoundationDocumentMetadata.from_dict(advisory_opc_foundation_document_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


