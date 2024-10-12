# AdvisoryAxis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_axis import AdvisoryAxis

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAxis from a JSON string
advisory_axis_instance = AdvisoryAxis.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAxis.to_json())

# convert the object into a dict
advisory_axis_dict = advisory_axis_instance.to_dict()
# create an instance of AdvisoryAxis from a dict
advisory_axis_from_dict = AdvisoryAxis.from_dict(advisory_axis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


