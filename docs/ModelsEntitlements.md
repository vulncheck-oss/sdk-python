# ModelsEntitlements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlements** | **Dict[str, List[str]]** | Entitlements provides a map of roles to a list of entitlements | [optional] 

## Example

```python
from vulncheck_sdk.models.models_entitlements import ModelsEntitlements

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsEntitlements from a JSON string
models_entitlements_instance = ModelsEntitlements.from_json(json)
# print the JSON string representation of the object
print(ModelsEntitlements.to_json())

# convert the object into a dict
models_entitlements_dict = models_entitlements_instance.to_dict()
# create an instance of ModelsEntitlements from a dict
models_entitlements_from_dict = ModelsEntitlements.from_dict(models_entitlements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


