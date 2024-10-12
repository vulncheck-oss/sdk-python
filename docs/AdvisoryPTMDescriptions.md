# AdvisoryPTMDescriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwe_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ptm_descriptions import AdvisoryPTMDescriptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPTMDescriptions from a JSON string
advisory_ptm_descriptions_instance = AdvisoryPTMDescriptions.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPTMDescriptions.to_json())

# convert the object into a dict
advisory_ptm_descriptions_dict = advisory_ptm_descriptions_instance.to_dict()
# create an instance of AdvisoryPTMDescriptions from a dict
advisory_ptm_descriptions_from_dict = AdvisoryPTMDescriptions.from_dict(advisory_ptm_descriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


