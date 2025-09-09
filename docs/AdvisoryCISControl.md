# AdvisoryCISControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cis_control_description** | **str** |  | [optional] 
**cis_control_id** | **str** |  | [optional] 
**cis_control_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cis_control import AdvisoryCISControl

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCISControl from a JSON string
advisory_cis_control_instance = AdvisoryCISControl.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCISControl.to_json())

# convert the object into a dict
advisory_cis_control_dict = advisory_cis_control_instance.to_dict()
# create an instance of AdvisoryCISControl from a dict
advisory_cis_control_from_dict = AdvisoryCISControl.from_dict(advisory_cis_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


