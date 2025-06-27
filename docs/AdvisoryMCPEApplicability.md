# AdvisoryMCPEApplicability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**negate** | **bool** |  | [optional] 
**nodes** | [**List[AdvisoryMNodes]**](AdvisoryMNodes.md) |  | [optional] 
**operator** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mcpe_applicability import AdvisoryMCPEApplicability

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMCPEApplicability from a JSON string
advisory_mcpe_applicability_instance = AdvisoryMCPEApplicability.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMCPEApplicability.to_json())

# convert the object into a dict
advisory_mcpe_applicability_dict = advisory_mcpe_applicability_instance.to_dict()
# create an instance of AdvisoryMCPEApplicability from a dict
advisory_mcpe_applicability_from_dict = AdvisoryMCPEApplicability.from_dict(advisory_mcpe_applicability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


