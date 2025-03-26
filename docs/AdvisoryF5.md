# AdvisoryF5


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
from vulncheck_sdk.models.advisory_f5 import AdvisoryF5

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryF5 from a JSON string
advisory_f5_instance = AdvisoryF5.from_json(json)
# print the JSON string representation of the object
print(AdvisoryF5.to_json())

# convert the object into a dict
advisory_f5_dict = advisory_f5_instance.to_dict()
# create an instance of AdvisoryF5 from a dict
advisory_f5_from_dict = AdvisoryF5.from_dict(advisory_f5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


