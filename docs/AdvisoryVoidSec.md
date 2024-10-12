# AdvisoryVoidSec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_void_sec import AdvisoryVoidSec

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVoidSec from a JSON string
advisory_void_sec_instance = AdvisoryVoidSec.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVoidSec.to_json())

# convert the object into a dict
advisory_void_sec_dict = advisory_void_sec_instance.to_dict()
# create an instance of AdvisoryVoidSec from a dict
advisory_void_sec_from_dict = AdvisoryVoidSec.from_dict(advisory_void_sec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


