# AdvisoryMDocumentTracking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_release_date** | **str** |  | [optional] 
**initial_release_date** | **str** |  | [optional] 
**identification** | [**AdvisoryMIdentification**](AdvisoryMIdentification.md) |  | [optional] 
**revisionhistory** | [**List[AdvisoryRRevision]**](AdvisoryRRevision.md) | diff in xml/json | [optional] 
**status** | **int** | again - change in json/xml | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_document_tracking import AdvisoryMDocumentTracking

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMDocumentTracking from a JSON string
advisory_m_document_tracking_instance = AdvisoryMDocumentTracking.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMDocumentTracking.to_json())

# convert the object into a dict
advisory_m_document_tracking_dict = advisory_m_document_tracking_instance.to_dict()
# create an instance of AdvisoryMDocumentTracking from a dict
advisory_m_document_tracking_from_dict = AdvisoryMDocumentTracking.from_dict(advisory_m_document_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


