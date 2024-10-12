# AdvisoryElspec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_elspec import AdvisoryElspec

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryElspec from a JSON string
advisory_elspec_instance = AdvisoryElspec.from_json(json)
# print the JSON string representation of the object
print(AdvisoryElspec.to_json())

# convert the object into a dict
advisory_elspec_dict = advisory_elspec_instance.to_dict()
# create an instance of AdvisoryElspec from a dict
advisory_elspec_from_dict = AdvisoryElspec.from_dict(advisory_elspec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


