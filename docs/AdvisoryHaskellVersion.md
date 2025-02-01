# AdvisoryHaskellVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed** | **str** |  | [optional] 
**introduced** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_haskell_version import AdvisoryHaskellVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHaskellVersion from a JSON string
advisory_haskell_version_instance = AdvisoryHaskellVersion.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHaskellVersion.to_json())

# convert the object into a dict
advisory_haskell_version_dict = advisory_haskell_version_instance.to_dict()
# create an instance of AdvisoryHaskellVersion from a dict
advisory_haskell_version_from_dict = AdvisoryHaskellVersion.from_dict(advisory_haskell_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


