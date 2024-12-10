# AdvisoryExternalReferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**source_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_external_references import AdvisoryExternalReferences

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryExternalReferences from a JSON string
advisory_external_references_instance = AdvisoryExternalReferences.from_json(json)
# print the JSON string representation of the object
print(AdvisoryExternalReferences.to_json())

# convert the object into a dict
advisory_external_references_dict = advisory_external_references_instance.to_dict()
# create an instance of AdvisoryExternalReferences from a dict
advisory_external_references_from_dict = AdvisoryExternalReferences.from_dict(advisory_external_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


