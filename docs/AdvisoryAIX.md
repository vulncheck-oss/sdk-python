# AdvisoryAIX


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_aix import AdvisoryAIX

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAIX from a JSON string
advisory_aix_instance = AdvisoryAIX.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAIX.to_json())

# convert the object into a dict
advisory_aix_dict = advisory_aix_instance.to_dict()
# create an instance of AdvisoryAIX from a dict
advisory_aix_from_dict = AdvisoryAIX.from_dict(advisory_aix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


