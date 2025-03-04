# AdvisoryAstra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bdu** | **List[str]** |  | [optional] 
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary_ru** | **str** |  | [optional] 
**title_ru** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_astra import AdvisoryAstra

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAstra from a JSON string
advisory_astra_instance = AdvisoryAstra.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAstra.to_json())

# convert the object into a dict
advisory_astra_dict = advisory_astra_instance.to_dict()
# create an instance of AdvisoryAstra from a dict
advisory_astra_from_dict = AdvisoryAstra.from_dict(advisory_astra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


