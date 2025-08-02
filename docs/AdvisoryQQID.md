# AdvisoryQQID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cvss3_score** | **str** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**qid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_qqid import AdvisoryQQID

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryQQID from a JSON string
advisory_qqid_instance = AdvisoryQQID.from_json(json)
# print the JSON string representation of the object
print(AdvisoryQQID.to_json())

# convert the object into a dict
advisory_qqid_dict = advisory_qqid_instance.to_dict()
# create an instance of AdvisoryQQID from a dict
advisory_qqid_from_dict = AdvisoryQQID.from_dict(advisory_qqid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


