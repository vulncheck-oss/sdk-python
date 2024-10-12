# AdvisorySSASource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**AdvisorySiemensDocument**](AdvisorySiemensDocument.md) |  | [optional] 
**product_tree** | [**AdvisorySiemensProductTree**](AdvisorySiemensProductTree.md) |  | [optional] 
**vulnerabilities** | [**List[AdvisorySiemensVulnerability]**](AdvisorySiemensVulnerability.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ssa_source import AdvisorySSASource

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySSASource from a JSON string
advisory_ssa_source_instance = AdvisorySSASource.from_json(json)
# print the JSON string representation of the object
print(AdvisorySSASource.to_json())

# convert the object into a dict
advisory_ssa_source_dict = advisory_ssa_source_instance.to_dict()
# create an instance of AdvisorySSASource from a dict
advisory_ssa_source_from_dict = AdvisorySSASource.from_dict(advisory_ssa_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


