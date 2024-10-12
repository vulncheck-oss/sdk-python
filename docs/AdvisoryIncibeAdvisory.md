# AdvisoryIncibeAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**solution** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_incibe_advisory import AdvisoryIncibeAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIncibeAdvisory from a JSON string
advisory_incibe_advisory_instance = AdvisoryIncibeAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIncibeAdvisory.to_json())

# convert the object into a dict
advisory_incibe_advisory_dict = advisory_incibe_advisory_instance.to_dict()
# create an instance of AdvisoryIncibeAdvisory from a dict
advisory_incibe_advisory_from_dict = AdvisoryIncibeAdvisory.from_dict(advisory_incibe_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


