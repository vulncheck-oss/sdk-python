# AdvisoryRockyFix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**source_by** | **str** |  | [optional] 
**source_link** | **str** |  | [optional] 
**ticket** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rocky_fix import AdvisoryRockyFix

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRockyFix from a JSON string
advisory_rocky_fix_instance = AdvisoryRockyFix.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRockyFix.to_json())

# convert the object into a dict
advisory_rocky_fix_dict = advisory_rocky_fix_instance.to_dict()
# create an instance of AdvisoryRockyFix from a dict
advisory_rocky_fix_from_dict = AdvisoryRockyFix.from_dict(advisory_rocky_fix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


