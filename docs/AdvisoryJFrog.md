# AdvisoryJFrog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpes** | [**List[AdvisoryNVD20CVECPEMatch]**](AdvisoryNVD20CVECPEMatch.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_j_frog import AdvisoryJFrog

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJFrog from a JSON string
advisory_j_frog_instance = AdvisoryJFrog.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJFrog.to_json())

# convert the object into a dict
advisory_j_frog_dict = advisory_j_frog_instance.to_dict()
# create an instance of AdvisoryJFrog from a dict
advisory_j_frog_from_dict = AdvisoryJFrog.from_dict(advisory_j_frog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


