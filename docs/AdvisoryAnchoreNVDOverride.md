# AdvisoryAnchoreNVDOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**override** | [**AdvisoryOverride**](AdvisoryOverride.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_anchore_nvd_override import AdvisoryAnchoreNVDOverride

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAnchoreNVDOverride from a JSON string
advisory_anchore_nvd_override_instance = AdvisoryAnchoreNVDOverride.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAnchoreNVDOverride.to_json())

# convert the object into a dict
advisory_anchore_nvd_override_dict = advisory_anchore_nvd_override_instance.to_dict()
# create an instance of AdvisoryAnchoreNVDOverride from a dict
advisory_anchore_nvd_override_from_dict = AdvisoryAnchoreNVDOverride.from_dict(advisory_anchore_nvd_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


