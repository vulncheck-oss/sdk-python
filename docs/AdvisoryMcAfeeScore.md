# AdvisoryMcAfeeScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | [optional] 
**cve** | **str** |  | [optional] 
**temporal** | **str** |  | [optional] 
**vector** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mc_afee_score import AdvisoryMcAfeeScore

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMcAfeeScore from a JSON string
advisory_mc_afee_score_instance = AdvisoryMcAfeeScore.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMcAfeeScore.to_json())

# convert the object into a dict
advisory_mc_afee_score_dict = advisory_mc_afee_score_instance.to_dict()
# create an instance of AdvisoryMcAfeeScore from a dict
advisory_mc_afee_score_from_dict = AdvisoryMcAfeeScore.from_dict(advisory_mc_afee_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


