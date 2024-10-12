# AdvisorySpring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_spring import AdvisorySpring

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySpring from a JSON string
advisory_spring_instance = AdvisorySpring.from_json(json)
# print the JSON string representation of the object
print(AdvisorySpring.to_json())

# convert the object into a dict
advisory_spring_dict = advisory_spring_instance.to_dict()
# create an instance of AdvisorySpring from a dict
advisory_spring_from_dict = AdvisorySpring.from_dict(advisory_spring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


