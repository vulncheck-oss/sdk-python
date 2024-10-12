# AdvisoryTI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**incident_id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ti import AdvisoryTI

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTI from a JSON string
advisory_ti_instance = AdvisoryTI.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTI.to_json())

# convert the object into a dict
advisory_ti_dict = advisory_ti_instance.to_dict()
# create an instance of AdvisoryTI from a dict
advisory_ti_from_dict = AdvisoryTI.from_dict(advisory_ti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


