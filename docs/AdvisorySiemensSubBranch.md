# AdvisorySiemensSubBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**List[AdvisorySiemensSubSubBranch]**](AdvisorySiemensSubSubBranch.md) |  | [optional] 
**category** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_sub_branch import AdvisorySiemensSubBranch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensSubBranch from a JSON string
advisory_siemens_sub_branch_instance = AdvisorySiemensSubBranch.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensSubBranch.to_json())

# convert the object into a dict
advisory_siemens_sub_branch_dict = advisory_siemens_sub_branch_instance.to_dict()
# create an instance of AdvisorySiemensSubBranch from a dict
advisory_siemens_sub_branch_from_dict = AdvisorySiemensSubBranch.from_dict(advisory_siemens_sub_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


