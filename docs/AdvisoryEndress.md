# AdvisoryEndress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_endress import AdvisoryEndress

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEndress from a JSON string
advisory_endress_instance = AdvisoryEndress.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEndress.to_json())

# convert the object into a dict
advisory_endress_dict = advisory_endress_instance.to_dict()
# create an instance of AdvisoryEndress from a dict
advisory_endress_from_dict = AdvisoryEndress.from_dict(advisory_endress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


