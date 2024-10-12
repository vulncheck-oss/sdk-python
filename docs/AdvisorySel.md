# AdvisorySel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgement** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sel import AdvisorySel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySel from a JSON string
advisory_sel_instance = AdvisorySel.from_json(json)
# print the JSON string representation of the object
print(AdvisorySel.to_json())

# convert the object into a dict
advisory_sel_dict = advisory_sel_instance.to_dict()
# create an instance of AdvisorySel from a dict
advisory_sel_from_dict = AdvisorySel.from_dict(advisory_sel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


