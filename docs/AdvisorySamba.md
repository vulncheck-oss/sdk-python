# AdvisorySamba


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**issues** | **str** |  | [optional] 
**patches** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_samba import AdvisorySamba

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySamba from a JSON string
advisory_samba_instance = AdvisorySamba.from_json(json)
# print the JSON string representation of the object
print(AdvisorySamba.to_json())

# convert the object into a dict
advisory_samba_dict = advisory_samba_instance.to_dict()
# create an instance of AdvisorySamba from a dict
advisory_samba_from_dict = AdvisorySamba.from_dict(advisory_samba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


