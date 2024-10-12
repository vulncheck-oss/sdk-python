# AdvisorySick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf_url** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sick import AdvisorySick

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySick from a JSON string
advisory_sick_instance = AdvisorySick.from_json(json)
# print the JSON string representation of the object
print(AdvisorySick.to_json())

# convert the object into a dict
advisory_sick_dict = advisory_sick_instance.to_dict()
# create an instance of AdvisorySick from a dict
advisory_sick_from_dict = AdvisorySick.from_dict(advisory_sick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


