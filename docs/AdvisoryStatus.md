# AdvisoryStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_status import AdvisoryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryStatus from a JSON string
advisory_status_instance = AdvisoryStatus.from_json(json)
# print the JSON string representation of the object
print(AdvisoryStatus.to_json())

# convert the object into a dict
advisory_status_dict = advisory_status_instance.to_dict()
# create an instance of AdvisoryStatus from a dict
advisory_status_from_dict = AdvisoryStatus.from_dict(advisory_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


