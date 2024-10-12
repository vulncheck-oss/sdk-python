# AdvisoryRestartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_restart_data import AdvisoryRestartData

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRestartData from a JSON string
advisory_restart_data_instance = AdvisoryRestartData.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRestartData.to_json())

# convert the object into a dict
advisory_restart_data_dict = advisory_restart_data_instance.to_dict()
# create an instance of AdvisoryRestartData from a dict
advisory_restart_data_from_dict = AdvisoryRestartData.from_dict(advisory_restart_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


