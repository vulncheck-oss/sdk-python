# AdvisoryUSOMAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**effect_tr** | **str** |  | [optional] 
**general_information_tr** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**solution_tr** | **str** |  | [optional] 
**title_tr** | **str** |  | [optional] 
**trid** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_usom_advisory import AdvisoryUSOMAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryUSOMAdvisory from a JSON string
advisory_usom_advisory_instance = AdvisoryUSOMAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryUSOMAdvisory.to_json())

# convert the object into a dict
advisory_usom_advisory_dict = advisory_usom_advisory_instance.to_dict()
# create an instance of AdvisoryUSOMAdvisory from a dict
advisory_usom_advisory_from_dict = AdvisoryUSOMAdvisory.from_dict(advisory_usom_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


