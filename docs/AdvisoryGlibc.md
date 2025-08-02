# AdvisoryGlibc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_glibc import AdvisoryGlibc

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGlibc from a JSON string
advisory_glibc_instance = AdvisoryGlibc.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGlibc.to_json())

# convert the object into a dict
advisory_glibc_dict = advisory_glibc_instance.to_dict()
# create an instance of AdvisoryGlibc from a dict
advisory_glibc_from_dict = AdvisoryGlibc.from_dict(advisory_glibc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


