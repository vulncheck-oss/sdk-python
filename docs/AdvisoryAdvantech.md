# AdvisoryAdvantech


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_advantech import AdvisoryAdvantech

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAdvantech from a JSON string
advisory_advantech_instance = AdvisoryAdvantech.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAdvantech.to_json())

# convert the object into a dict
advisory_advantech_dict = advisory_advantech_instance.to_dict()
# create an instance of AdvisoryAdvantech from a dict
advisory_advantech_from_dict = AdvisoryAdvantech.from_dict(advisory_advantech_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


