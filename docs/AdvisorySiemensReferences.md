# AdvisorySiemensReferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_references import AdvisorySiemensReferences

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensReferences from a JSON string
advisory_siemens_references_instance = AdvisorySiemensReferences.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensReferences.to_json())

# convert the object into a dict
advisory_siemens_references_dict = advisory_siemens_references_instance.to_dict()
# create an instance of AdvisorySiemensReferences from a dict
advisory_siemens_references_from_dict = AdvisorySiemensReferences.from_dict(advisory_siemens_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


