# AdvisorySiemensAcknowledgments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** |  | [optional] 
**organization** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_acknowledgments import AdvisorySiemensAcknowledgments

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensAcknowledgments from a JSON string
advisory_siemens_acknowledgments_instance = AdvisorySiemensAcknowledgments.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensAcknowledgments.to_json())

# convert the object into a dict
advisory_siemens_acknowledgments_dict = advisory_siemens_acknowledgments_instance.to_dict()
# create an instance of AdvisorySiemensAcknowledgments from a dict
advisory_siemens_acknowledgments_from_dict = AdvisorySiemensAcknowledgments.from_dict(advisory_siemens_acknowledgments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


