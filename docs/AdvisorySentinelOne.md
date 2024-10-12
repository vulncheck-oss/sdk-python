# AdvisorySentinelOne


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sentinel_one import AdvisorySentinelOne

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySentinelOne from a JSON string
advisory_sentinel_one_instance = AdvisorySentinelOne.from_json(json)
# print the JSON string representation of the object
print(AdvisorySentinelOne.to_json())

# convert the object into a dict
advisory_sentinel_one_dict = advisory_sentinel_one_instance.to_dict()
# create an instance of AdvisorySentinelOne from a dict
advisory_sentinel_one_from_dict = AdvisorySentinelOne.from_dict(advisory_sentinel_one_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


