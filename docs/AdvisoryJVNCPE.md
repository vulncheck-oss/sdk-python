# AdvisoryJVNCPE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_jvncpe import AdvisoryJVNCPE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJVNCPE from a JSON string
advisory_jvncpe_instance = AdvisoryJVNCPE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJVNCPE.to_json())

# convert the object into a dict
advisory_jvncpe_dict = advisory_jvncpe_instance.to_dict()
# create an instance of AdvisoryJVNCPE from a dict
advisory_jvncpe_from_dict = AdvisoryJVNCPE.from_dict(advisory_jvncpe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


