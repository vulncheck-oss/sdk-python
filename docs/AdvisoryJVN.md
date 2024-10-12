# AdvisoryJVN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_en** | **str** |  | [optional] 
**affected_ja** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description_en** | **str** |  | [optional] 
**description_ja** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**solution_en** | **str** |  | [optional] 
**solution_ja** | **str** |  | [optional] 
**summary_en** | **str** |  | [optional] 
**summary_ja** | **str** |  | [optional] 
**title_en** | **str** |  | [optional] 
**title_ja** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_jvn import AdvisoryJVN

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJVN from a JSON string
advisory_jvn_instance = AdvisoryJVN.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJVN.to_json())

# convert the object into a dict
advisory_jvn_dict = advisory_jvn_instance.to_dict()
# create an instance of AdvisoryJVN from a dict
advisory_jvn_from_dict = AdvisoryJVN.from_dict(advisory_jvn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


