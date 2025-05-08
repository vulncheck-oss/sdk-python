# AdvisoryWordfence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_wordfence import AdvisoryWordfence

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWordfence from a JSON string
advisory_wordfence_instance = AdvisoryWordfence.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWordfence.to_json())

# convert the object into a dict
advisory_wordfence_dict = advisory_wordfence_instance.to_dict()
# create an instance of AdvisoryWordfence from a dict
advisory_wordfence_from_dict = AdvisoryWordfence.from_dict(advisory_wordfence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


