# AdvisoryTracking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_release_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**initial_release_date** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tracking import AdvisoryTracking

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTracking from a JSON string
advisory_tracking_instance = AdvisoryTracking.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTracking.to_json())

# convert the object into a dict
advisory_tracking_dict = advisory_tracking_instance.to_dict()
# create an instance of AdvisoryTracking from a dict
advisory_tracking_from_dict = AdvisoryTracking.from_dict(advisory_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


