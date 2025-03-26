# AdvisoryMcAfee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**mcafee_score** | [**List[AdvisoryMcAfeeScore]**](AdvisoryMcAfeeScore.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mc_afee import AdvisoryMcAfee

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMcAfee from a JSON string
advisory_mc_afee_instance = AdvisoryMcAfee.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMcAfee.to_json())

# convert the object into a dict
advisory_mc_afee_dict = advisory_mc_afee_instance.to_dict()
# create an instance of AdvisoryMcAfee from a dict
advisory_mc_afee_from_dict = AdvisoryMcAfee.from_dict(advisory_mc_afee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


