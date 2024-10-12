# AdvisorySiemensRemediation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**product_ids** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_remediation import AdvisorySiemensRemediation

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensRemediation from a JSON string
advisory_siemens_remediation_instance = AdvisorySiemensRemediation.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensRemediation.to_json())

# convert the object into a dict
advisory_siemens_remediation_dict = advisory_siemens_remediation_instance.to_dict()
# create an instance of AdvisorySiemensRemediation from a dict
advisory_siemens_remediation_from_dict = AdvisorySiemensRemediation.from_dict(advisory_siemens_remediation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


