# AdvisoryAppgate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_appgate import AdvisoryAppgate

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAppgate from a JSON string
advisory_appgate_instance = AdvisoryAppgate.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAppgate.to_json())

# convert the object into a dict
advisory_appgate_dict = advisory_appgate_instance.to_dict()
# create an instance of AdvisoryAppgate from a dict
advisory_appgate_from_dict = AdvisoryAppgate.from_dict(advisory_appgate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


