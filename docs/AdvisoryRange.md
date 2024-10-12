# AdvisoryRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AdvisoryEvent]**](AdvisoryEvent.md) |  | [optional] 
**repo** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_range import AdvisoryRange

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRange from a JSON string
advisory_range_instance = AdvisoryRange.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRange.to_json())

# convert the object into a dict
advisory_range_dict = advisory_range_instance.to_dict()
# create an instance of AdvisoryRange from a dict
advisory_range_from_dict = AdvisoryRange.from_dict(advisory_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


