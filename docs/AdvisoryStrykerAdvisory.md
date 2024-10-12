# AdvisoryStrykerAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_components** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_stryker_advisory import AdvisoryStrykerAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryStrykerAdvisory from a JSON string
advisory_stryker_advisory_instance = AdvisoryStrykerAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryStrykerAdvisory.to_json())

# convert the object into a dict
advisory_stryker_advisory_dict = advisory_stryker_advisory_instance.to_dict()
# create an instance of AdvisoryStrykerAdvisory from a dict
advisory_stryker_advisory_from_dict = AdvisoryStrykerAdvisory.from_dict(advisory_stryker_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


