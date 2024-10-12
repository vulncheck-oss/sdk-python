# AdvisoryASRG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**capec** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**problem_type** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_asrg import AdvisoryASRG

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryASRG from a JSON string
advisory_asrg_instance = AdvisoryASRG.from_json(json)
# print the JSON string representation of the object
print(AdvisoryASRG.to_json())

# convert the object into a dict
advisory_asrg_dict = advisory_asrg_instance.to_dict()
# create an instance of AdvisoryASRG from a dict
advisory_asrg_from_dict = AdvisoryASRG.from_dict(advisory_asrg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


