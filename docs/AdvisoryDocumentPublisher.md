# AdvisoryDocumentPublisher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_details** | **str** |  | [optional] 
**issuing_authority** | **str** |  | [optional] 
**type** | **int** | the json for this is missing/broke | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_document_publisher import AdvisoryDocumentPublisher

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDocumentPublisher from a JSON string
advisory_document_publisher_instance = AdvisoryDocumentPublisher.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDocumentPublisher.to_json())

# convert the object into a dict
advisory_document_publisher_dict = advisory_document_publisher_instance.to_dict()
# create an instance of AdvisoryDocumentPublisher from a dict
advisory_document_publisher_from_dict = AdvisoryDocumentPublisher.from_dict(advisory_document_publisher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


