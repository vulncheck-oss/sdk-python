# AdvisoryTrackingID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_name** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tracking_id import AdvisoryTrackingID

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTrackingID from a JSON string
advisory_tracking_id_instance = AdvisoryTrackingID.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTrackingID.to_json())

# convert the object into a dict
advisory_tracking_id_dict = advisory_tracking_id_instance.to_dict()
# create an instance of AdvisoryTrackingID from a dict
advisory_tracking_id_from_dict = AdvisoryTrackingID.from_dict(advisory_tracking_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


