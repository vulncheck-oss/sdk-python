# AdvisoryDassault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**affected_versions** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_dassault import AdvisoryDassault

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDassault from a JSON string
advisory_dassault_instance = AdvisoryDassault.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDassault.to_json())

# convert the object into a dict
advisory_dassault_dict = advisory_dassault_instance.to_dict()
# create an instance of AdvisoryDassault from a dict
advisory_dassault_from_dict = AdvisoryDassault.from_dict(advisory_dassault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


