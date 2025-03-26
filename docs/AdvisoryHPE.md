# AdvisoryHPE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hpe import AdvisoryHPE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHPE from a JSON string
advisory_hpe_instance = AdvisoryHPE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHPE.to_json())

# convert the object into a dict
advisory_hpe_dict = advisory_hpe_instance.to_dict()
# create an instance of AdvisoryHPE from a dict
advisory_hpe_from_dict = AdvisoryHPE.from_dict(advisory_hpe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


