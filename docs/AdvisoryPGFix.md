# AdvisoryPGFix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_pg_fix import AdvisoryPGFix

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPGFix from a JSON string
advisory_pg_fix_instance = AdvisoryPGFix.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPGFix.to_json())

# convert the object into a dict
advisory_pg_fix_dict = advisory_pg_fix_instance.to_dict()
# create an instance of AdvisoryPGFix from a dict
advisory_pg_fix_from_dict = AdvisoryPGFix.from_dict(advisory_pg_fix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


