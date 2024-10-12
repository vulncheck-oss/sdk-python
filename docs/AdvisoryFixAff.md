# AdvisoryFixAff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_since** | **str** |  | [optional] 
**fixed_version** | **str** |  | [optional] 
**patch_url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_fix_aff import AdvisoryFixAff

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFixAff from a JSON string
advisory_fix_aff_instance = AdvisoryFixAff.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFixAff.to_json())

# convert the object into a dict
advisory_fix_aff_dict = advisory_fix_aff_instance.to_dict()
# create an instance of AdvisoryFixAff from a dict
advisory_fix_aff_from_dict = AdvisoryFixAff.from_dict(advisory_fix_aff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


