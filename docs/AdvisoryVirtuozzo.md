# AdvisoryVirtuozzo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_virtuozzo import AdvisoryVirtuozzo

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVirtuozzo from a JSON string
advisory_virtuozzo_instance = AdvisoryVirtuozzo.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVirtuozzo.to_json())

# convert the object into a dict
advisory_virtuozzo_dict = advisory_virtuozzo_instance.to_dict()
# create an instance of AdvisoryVirtuozzo from a dict
advisory_virtuozzo_from_dict = AdvisoryVirtuozzo.from_dict(advisory_virtuozzo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


