# AdvisoryHP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hp import AdvisoryHP

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHP from a JSON string
advisory_hp_instance = AdvisoryHP.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHP.to_json())

# convert the object into a dict
advisory_hp_dict = advisory_hp_instance.to_dict()
# create an instance of AdvisoryHP from a dict
advisory_hp_from_dict = AdvisoryHP.from_dict(advisory_hp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


