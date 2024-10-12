# AdvisoryGallagher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_exploitation** | **bool** |  | [optional] 
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fixes** | **str** |  | [optional] 
**reported_by** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gallagher import AdvisoryGallagher

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGallagher from a JSON string
advisory_gallagher_instance = AdvisoryGallagher.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGallagher.to_json())

# convert the object into a dict
advisory_gallagher_dict = advisory_gallagher_instance.to_dict()
# create an instance of AdvisoryGallagher from a dict
advisory_gallagher_from_dict = AdvisoryGallagher.from_dict(advisory_gallagher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


