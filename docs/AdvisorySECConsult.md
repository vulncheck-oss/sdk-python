# AdvisorySECConsult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sec_consult import AdvisorySECConsult

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySECConsult from a JSON string
advisory_sec_consult_instance = AdvisorySECConsult.from_json(json)
# print the JSON string representation of the object
print(AdvisorySECConsult.to_json())

# convert the object into a dict
advisory_sec_consult_dict = advisory_sec_consult_instance.to_dict()
# create an instance of AdvisorySECConsult from a dict
advisory_sec_consult_from_dict = AdvisorySECConsult.from_dict(advisory_sec_consult_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


