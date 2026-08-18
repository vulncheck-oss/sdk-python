# ApiNVD20SsvcDecisionTree

nvd doesn't populate this field. at least as of this commit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision_points** | [**List[ApiNVD20SsvcDecisionPoint]**](ApiNVD20SsvcDecisionPoint.md) |  | [optional] 
**decisions_table** | **List[List[int]]** | DecisionsTable is an array of objects with no declared properties, so there is nothing to model. In practice each entry maps decision point labels to the chosen option, plus the resulting outcome. | [optional] 
**lang** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_ssvc_decision_tree import ApiNVD20SsvcDecisionTree

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20SsvcDecisionTree from a JSON string
api_nvd20_ssvc_decision_tree_instance = ApiNVD20SsvcDecisionTree.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20SsvcDecisionTree.to_json())

# convert the object into a dict
api_nvd20_ssvc_decision_tree_dict = api_nvd20_ssvc_decision_tree_instance.to_dict()
# create an instance of ApiNVD20SsvcDecisionTree from a dict
api_nvd20_ssvc_decision_tree_from_dict = ApiNVD20SsvcDecisionTree.from_dict(api_nvd20_ssvc_decision_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


