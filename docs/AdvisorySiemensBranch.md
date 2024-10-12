# AdvisorySiemensBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**List[AdvisorySiemensSubBranch]**](AdvisorySiemensSubBranch.md) |  | [optional] 
**category** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_branch import AdvisorySiemensBranch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensBranch from a JSON string
advisory_siemens_branch_instance = AdvisorySiemensBranch.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensBranch.to_json())

# convert the object into a dict
advisory_siemens_branch_dict = advisory_siemens_branch_instance.to_dict()
# create an instance of AdvisorySiemensBranch from a dict
advisory_siemens_branch_from_dict = AdvisorySiemensBranch.from_dict(advisory_siemens_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


