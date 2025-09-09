# AdvisoryNISTControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cis_controls** | [**List[AdvisoryCISControl]**](AdvisoryCISControl.md) |  | [optional] 
**nist_control_family** | **str** |  | [optional] 
**nist_control_id** | **str** |  | [optional] 
**nist_control_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nist_control import AdvisoryNISTControl

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNISTControl from a JSON string
advisory_nist_control_instance = AdvisoryNISTControl.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNISTControl.to_json())

# convert the object into a dict
advisory_nist_control_dict = advisory_nist_control_instance.to_dict()
# create an instance of AdvisoryNISTControl from a dict
advisory_nist_control_from_dict = AdvisoryNISTControl.from_dict(advisory_nist_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


