# AdvisorySafran


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_safran import AdvisorySafran

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySafran from a JSON string
advisory_safran_instance = AdvisorySafran.from_json(json)
# print the JSON string representation of the object
print(AdvisorySafran.to_json())

# convert the object into a dict
advisory_safran_dict = advisory_safran_instance.to_dict()
# create an instance of AdvisorySafran from a dict
advisory_safran_from_dict = AdvisorySafran.from_dict(advisory_safran_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


