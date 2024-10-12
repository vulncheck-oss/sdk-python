# AdvisorySiemensDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgments** | [**List[AdvisorySiemensAcknowledgments]**](AdvisorySiemensAcknowledgments.md) |  | [optional] 
**category** | **str** |  | [optional] 
**csaf_version** | **str** |  | [optional] 
**distribution** | [**AdvisorySiemensDistribution**](AdvisorySiemensDistribution.md) |  | [optional] 
**notes** | [**List[AdvisorySiemensNotes]**](AdvisorySiemensNotes.md) |  | [optional] 
**publisher** | [**AdvisorySiemensPublisher**](AdvisorySiemensPublisher.md) |  | [optional] 
**references** | [**List[AdvisorySiemensReferences]**](AdvisorySiemensReferences.md) |  | [optional] 
**title** | **str** |  | [optional] 
**tracking** | [**AdvisorySiemensTracking**](AdvisorySiemensTracking.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_document import AdvisorySiemensDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensDocument from a JSON string
advisory_siemens_document_instance = AdvisorySiemensDocument.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensDocument.to_json())

# convert the object into a dict
advisory_siemens_document_dict = advisory_siemens_document_instance.to_dict()
# create an instance of AdvisorySiemensDocument from a dict
advisory_siemens_document_from_dict = AdvisorySiemensDocument.from_dict(advisory_siemens_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


