# AdvisorySAAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**threats** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**warning_date** | **str** |  | [optional] 
**warning_number** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sa_advisory import AdvisorySAAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySAAdvisory from a JSON string
advisory_sa_advisory_instance = AdvisorySAAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySAAdvisory.to_json())

# convert the object into a dict
advisory_sa_advisory_dict = advisory_sa_advisory_instance.to_dict()
# create an instance of AdvisorySAAdvisory from a dict
advisory_sa_advisory_from_dict = AdvisorySAAdvisory.from_dict(advisory_sa_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


