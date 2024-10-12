# AdvisoryDocumentTracking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_release_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**initial_release_date** | **str** |  | [optional] 
**revision_history** | [**List[AdvisoryRevision]**](AdvisoryRevision.md) |  | [optional] 
**status** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_document_tracking import AdvisoryDocumentTracking

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDocumentTracking from a JSON string
advisory_document_tracking_instance = AdvisoryDocumentTracking.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDocumentTracking.to_json())

# convert the object into a dict
advisory_document_tracking_dict = advisory_document_tracking_instance.to_dict()
# create an instance of AdvisoryDocumentTracking from a dict
advisory_document_tracking_from_dict = AdvisoryDocumentTracking.from_dict(advisory_document_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


