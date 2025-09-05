# AdvisoryCweData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cwe_data import AdvisoryCweData

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCweData from a JSON string
advisory_cwe_data_instance = AdvisoryCweData.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCweData.to_json())

# convert the object into a dict
advisory_cwe_data_dict = advisory_cwe_data_instance.to_dict()
# create an instance of AdvisoryCweData from a dict
advisory_cwe_data_from_dict = AdvisoryCweData.from_dict(advisory_cwe_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


