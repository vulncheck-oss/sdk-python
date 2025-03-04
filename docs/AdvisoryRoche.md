# AdvisoryRoche


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**roche_cves** | [**List[AdvisoryRocheCVE]**](AdvisoryRocheCVE.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_roche import AdvisoryRoche

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRoche from a JSON string
advisory_roche_instance = AdvisoryRoche.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRoche.to_json())

# convert the object into a dict
advisory_roche_dict = advisory_roche_instance.to_dict()
# create an instance of AdvisoryRoche from a dict
advisory_roche_from_dict = AdvisoryRoche.from_dict(advisory_roche_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


