# AdvisoryWRT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | **str** |  | [optional] 
**affected_versions** | **str** |  | [optional] 
**credits** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**mitigations** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**requirements** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_wrt import AdvisoryWRT

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWRT from a JSON string
advisory_wrt_instance = AdvisoryWRT.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWRT.to_json())

# convert the object into a dict
advisory_wrt_dict = advisory_wrt_instance.to_dict()
# create an instance of AdvisoryWRT from a dict
advisory_wrt_from_dict = AdvisoryWRT.from_dict(advisory_wrt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


