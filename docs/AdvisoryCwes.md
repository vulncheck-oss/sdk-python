# AdvisoryCwes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[AdvisoryCWENode]**](AdvisoryCWENode.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cwes import AdvisoryCwes

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCwes from a JSON string
advisory_cwes_instance = AdvisoryCwes.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCwes.to_json())

# convert the object into a dict
advisory_cwes_dict = advisory_cwes_instance.to_dict()
# create an instance of AdvisoryCwes from a dict
advisory_cwes_from_dict = AdvisoryCwes.from_dict(advisory_cwes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


