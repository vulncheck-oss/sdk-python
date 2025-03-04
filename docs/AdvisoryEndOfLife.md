# AdvisoryEndOfLife


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cycles** | [**List[AdvisoryCycle]**](AdvisoryCycle.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_end_of_life import AdvisoryEndOfLife

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEndOfLife from a JSON string
advisory_end_of_life_instance = AdvisoryEndOfLife.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEndOfLife.to_json())

# convert the object into a dict
advisory_end_of_life_dict = advisory_end_of_life_instance.to_dict()
# create an instance of AdvisoryEndOfLife from a dict
advisory_end_of_life_from_dict = AdvisoryEndOfLife.from_dict(advisory_end_of_life_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


