# AdvisorySudo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**fix** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**workaround** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sudo import AdvisorySudo

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySudo from a JSON string
advisory_sudo_instance = AdvisorySudo.from_json(json)
# print the JSON string representation of the object
print(AdvisorySudo.to_json())

# convert the object into a dict
advisory_sudo_dict = advisory_sudo_instance.to_dict()
# create an instance of AdvisorySudo from a dict
advisory_sudo_from_dict = AdvisorySudo.from_dict(advisory_sudo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


