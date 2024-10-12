# AdvisoryAppleComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_for** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**itw_exploit** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apple_component import AdvisoryAppleComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAppleComponent from a JSON string
advisory_apple_component_instance = AdvisoryAppleComponent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAppleComponent.to_json())

# convert the object into a dict
advisory_apple_component_dict = advisory_apple_component_instance.to_dict()
# create an instance of AdvisoryAppleComponent from a dict
advisory_apple_component_from_dict = AdvisoryAppleComponent.from_dict(advisory_apple_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


