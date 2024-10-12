# AdvisoryCheckPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_check_point import AdvisoryCheckPoint

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCheckPoint from a JSON string
advisory_check_point_instance = AdvisoryCheckPoint.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCheckPoint.to_json())

# convert the object into a dict
advisory_check_point_dict = advisory_check_point_instance.to_dict()
# create an instance of AdvisoryCheckPoint from a dict
advisory_check_point_from_dict = AdvisoryCheckPoint.from_dict(advisory_check_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


