# AdvisoryZeroScienceAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**affected_versions** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**po_c** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**risk** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zero_science_advisory import AdvisoryZeroScienceAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZeroScienceAdvisory from a JSON string
advisory_zero_science_advisory_instance = AdvisoryZeroScienceAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZeroScienceAdvisory.to_json())

# convert the object into a dict
advisory_zero_science_advisory_dict = advisory_zero_science_advisory_instance.to_dict()
# create an instance of AdvisoryZeroScienceAdvisory from a dict
advisory_zero_science_advisory_from_dict = AdvisoryZeroScienceAdvisory.from_dict(advisory_zero_science_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


