# AdvisoryRScoreSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**temporal_score** | **str** |  | [optional] 
**vector** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_r_score_set import AdvisoryRScoreSet

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRScoreSet from a JSON string
advisory_r_score_set_instance = AdvisoryRScoreSet.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRScoreSet.to_json())

# convert the object into a dict
advisory_r_score_set_dict = advisory_r_score_set_instance.to_dict()
# create an instance of AdvisoryRScoreSet from a dict
advisory_r_score_set_from_dict = AdvisoryRScoreSet.from_dict(advisory_r_score_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


