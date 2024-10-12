# AdvisoryChainGuardSecFix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_chain_guard_sec_fix import AdvisoryChainGuardSecFix

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryChainGuardSecFix from a JSON string
advisory_chain_guard_sec_fix_instance = AdvisoryChainGuardSecFix.from_json(json)
# print the JSON string representation of the object
print(AdvisoryChainGuardSecFix.to_json())

# convert the object into a dict
advisory_chain_guard_sec_fix_dict = advisory_chain_guard_sec_fix_instance.to_dict()
# create an instance of AdvisoryChainGuardSecFix from a dict
advisory_chain_guard_sec_fix_from_dict = AdvisoryChainGuardSecFix.from_dict(advisory_chain_guard_sec_fix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


