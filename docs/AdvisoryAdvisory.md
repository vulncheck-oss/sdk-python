# AdvisoryAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affects** | **str** |  | [optional] 
**announced** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**corrections** | [**List[AdvisoryCorrection]**](AdvisoryCorrection.md) |  | [optional] 
**credits** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**module** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**topic** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_advisory import AdvisoryAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAdvisory from a JSON string
advisory_advisory_instance = AdvisoryAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAdvisory.to_json())

# convert the object into a dict
advisory_advisory_dict = advisory_advisory_instance.to_dict()
# create an instance of AdvisoryAdvisory from a dict
advisory_advisory_from_dict = AdvisoryAdvisory.from_dict(advisory_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


