# AdvisoryVapidLabsAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**exploit** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**vapid_id** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**vulnerability** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vapid_labs_advisory import AdvisoryVapidLabsAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVapidLabsAdvisory from a JSON string
advisory_vapid_labs_advisory_instance = AdvisoryVapidLabsAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVapidLabsAdvisory.to_json())

# convert the object into a dict
advisory_vapid_labs_advisory_dict = advisory_vapid_labs_advisory_instance.to_dict()
# create an instance of AdvisoryVapidLabsAdvisory from a dict
advisory_vapid_labs_advisory_from_dict = AdvisoryVapidLabsAdvisory.from_dict(advisory_vapid_labs_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


