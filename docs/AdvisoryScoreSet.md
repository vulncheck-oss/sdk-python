# AdvisoryScoreSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **str** |  | [optional] 
**vector** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_score_set import AdvisoryScoreSet

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryScoreSet from a JSON string
advisory_score_set_instance = AdvisoryScoreSet.from_json(json)
# print the JSON string representation of the object
print(AdvisoryScoreSet.to_json())

# convert the object into a dict
advisory_score_set_dict = advisory_score_set_instance.to_dict()
# create an instance of AdvisoryScoreSet from a dict
advisory_score_set_from_dict = AdvisoryScoreSet.from_dict(advisory_score_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


