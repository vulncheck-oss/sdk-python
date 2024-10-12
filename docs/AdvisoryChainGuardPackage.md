# AdvisoryChainGuardPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**secfixes** | [**List[AdvisoryChainGuardSecFix]**](AdvisoryChainGuardSecFix.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_chain_guard_package import AdvisoryChainGuardPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryChainGuardPackage from a JSON string
advisory_chain_guard_package_instance = AdvisoryChainGuardPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryChainGuardPackage.to_json())

# convert the object into a dict
advisory_chain_guard_package_dict = advisory_chain_guard_package_instance.to_dict()
# create an instance of AdvisoryChainGuardPackage from a dict
advisory_chain_guard_package_from_dict = AdvisoryChainGuardPackage.from_dict(advisory_chain_guard_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


