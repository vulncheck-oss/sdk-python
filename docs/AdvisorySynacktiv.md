# AdvisorySynacktiv


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
from vulncheck_sdk.models.advisory_synacktiv import AdvisorySynacktiv

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySynacktiv from a JSON string
advisory_synacktiv_instance = AdvisorySynacktiv.from_json(json)
# print the JSON string representation of the object
print(AdvisorySynacktiv.to_json())

# convert the object into a dict
advisory_synacktiv_dict = advisory_synacktiv_instance.to_dict()
# create an instance of AdvisorySynacktiv from a dict
advisory_synacktiv_from_dict = AdvisorySynacktiv.from_dict(advisory_synacktiv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


