# AdvisoryTencent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary_cn** | **str** |  | [optional] 
**title_cn** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tencent import AdvisoryTencent

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTencent from a JSON string
advisory_tencent_instance = AdvisoryTencent.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTencent.to_json())

# convert the object into a dict
advisory_tencent_dict = advisory_tencent_instance.to_dict()
# create an instance of AdvisoryTencent from a dict
advisory_tencent_from_dict = AdvisoryTencent.from_dict(advisory_tencent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


