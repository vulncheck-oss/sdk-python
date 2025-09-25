# AdvisoryJohnsonControls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_johnson_controls import AdvisoryJohnsonControls

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJohnsonControls from a JSON string
advisory_johnson_controls_instance = AdvisoryJohnsonControls.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJohnsonControls.to_json())

# convert the object into a dict
advisory_johnson_controls_dict = advisory_johnson_controls_instance.to_dict()
# create an instance of AdvisoryJohnsonControls from a dict
advisory_johnson_controls_from_dict = AdvisoryJohnsonControls.from_dict(advisory_johnson_controls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


