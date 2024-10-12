# AdvisorySiemensTracking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_release_date** | **str** |  | [optional] 
**generator** | [**AdvisorySiemensGenerator**](AdvisorySiemensGenerator.md) |  | [optional] 
**id** | **str** |  | [optional] 
**initial_release_date** | **str** |  | [optional] 
**revision_history** | [**List[AdvisorySiemensRevisionHistory]**](AdvisorySiemensRevisionHistory.md) |  | [optional] 
**status** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_tracking import AdvisorySiemensTracking

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensTracking from a JSON string
advisory_siemens_tracking_instance = AdvisorySiemensTracking.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensTracking.to_json())

# convert the object into a dict
advisory_siemens_tracking_dict = advisory_siemens_tracking_instance.to_dict()
# create an instance of AdvisorySiemensTracking from a dict
advisory_siemens_tracking_from_dict = AdvisorySiemensTracking.from_dict(advisory_siemens_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


