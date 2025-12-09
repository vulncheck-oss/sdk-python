# AdvisoryAppleAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**components** | [**List[AdvisoryAppleComponent]**](AdvisoryAppleComponent.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apple_advisory import AdvisoryAppleAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAppleAdvisory from a JSON string
advisory_apple_advisory_instance = AdvisoryAppleAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAppleAdvisory.to_json())

# convert the object into a dict
advisory_apple_advisory_dict = advisory_apple_advisory_instance.to_dict()
# create an instance of AdvisoryAppleAdvisory from a dict
advisory_apple_advisory_from_dict = AdvisoryAppleAdvisory.from_dict(advisory_apple_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


