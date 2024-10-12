# AdvisoryChainGuard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apkurl** | **str** |  | [optional] 
**archs** | **List[str]** |  | [optional] 
**date_added** | **str** | un-used | [optional] 
**packages** | [**List[AdvisoryChainGuardPackage]**](AdvisoryChainGuardPackage.md) |  | [optional] 
**reponame** | **str** |  | [optional] 
**urlprefix** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_chain_guard import AdvisoryChainGuard

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryChainGuard from a JSON string
advisory_chain_guard_instance = AdvisoryChainGuard.from_json(json)
# print the JSON string representation of the object
print(AdvisoryChainGuard.to_json())

# convert the object into a dict
advisory_chain_guard_dict = advisory_chain_guard_instance.to_dict()
# create an instance of AdvisoryChainGuard from a dict
advisory_chain_guard_from_dict = AdvisoryChainGuard.from_dict(advisory_chain_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


