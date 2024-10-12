# AdvisoryCVEDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **str** |  | [optional] 
**cveid** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**vector** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cve_detail import AdvisoryCVEDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVEDetail from a JSON string
advisory_cve_detail_instance = AdvisoryCVEDetail.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVEDetail.to_json())

# convert the object into a dict
advisory_cve_detail_dict = advisory_cve_detail_instance.to_dict()
# create an instance of AdvisoryCVEDetail from a dict
advisory_cve_detail_from_dict = AdvisoryCVEDetail.from_dict(advisory_cve_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


