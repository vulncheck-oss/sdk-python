# AdvisoryLogSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**definition** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**service** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_log_source import AdvisoryLogSource

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryLogSource from a JSON string
advisory_log_source_instance = AdvisoryLogSource.from_json(json)
# print the JSON string representation of the object
print(AdvisoryLogSource.to_json())

# convert the object into a dict
advisory_log_source_dict = advisory_log_source_instance.to_dict()
# create an instance of AdvisoryLogSource from a dict
advisory_log_source_from_dict = AdvisoryLogSource.from_dict(advisory_log_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


