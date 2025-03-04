# AdvisoryCycle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codename** | **str** |  | [optional] 
**cycle** | **str** |  | [optional] 
**discontinued** | **object** |  | [optional] 
**eol** | **object** |  | [optional] 
**extended_support** | **object** |  | [optional] 
**latest** | **str** |  | [optional] 
**latest_release_date** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**lts** | **object** |  | [optional] 
**release_date** | **str** |  | [optional] 
**release_label** | **str** |  | [optional] 
**support** | **object** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cycle import AdvisoryCycle

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCycle from a JSON string
advisory_cycle_instance = AdvisoryCycle.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCycle.to_json())

# convert the object into a dict
advisory_cycle_dict = advisory_cycle_instance.to_dict()
# create an instance of AdvisoryCycle from a dict
advisory_cycle_from_dict = AdvisoryCycle.from_dict(advisory_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


