# AdvisoryA10


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**reference** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_a10 import AdvisoryA10

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryA10 from a JSON string
advisory_a10_instance = AdvisoryA10.from_json(json)
# print the JSON string representation of the object
print(AdvisoryA10.to_json())

# convert the object into a dict
advisory_a10_dict = advisory_a10_instance.to_dict()
# create an instance of AdvisoryA10 from a dict
advisory_a10_from_dict = AdvisoryA10.from_dict(advisory_a10_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


