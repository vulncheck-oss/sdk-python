# AdvisorySSDAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | **str** |  | [optional] 
**credit** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**poc** | **str** | contains actual poc code | [optional] 
**published** | **str** |  | [optional] 
**response_ref** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ssd_advisory import AdvisorySSDAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySSDAdvisory from a JSON string
advisory_ssd_advisory_instance = AdvisorySSDAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySSDAdvisory.to_json())

# convert the object into a dict
advisory_ssd_advisory_dict = advisory_ssd_advisory_instance.to_dict()
# create an instance of AdvisorySSDAdvisory from a dict
advisory_ssd_advisory_from_dict = AdvisorySSDAdvisory.from_dict(advisory_ssd_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


