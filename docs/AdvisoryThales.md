# AdvisoryThales


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_thales import AdvisoryThales

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryThales from a JSON string
advisory_thales_instance = AdvisoryThales.from_json(json)
# print the JSON string representation of the object
print(AdvisoryThales.to_json())

# convert the object into a dict
advisory_thales_dict = advisory_thales_instance.to_dict()
# create an instance of AdvisoryThales from a dict
advisory_thales_from_dict = AdvisoryThales.from_dict(advisory_thales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


