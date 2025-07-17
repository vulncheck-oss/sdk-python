# AdvisoryThermoFisher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_thermo_fisher import AdvisoryThermoFisher

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryThermoFisher from a JSON string
advisory_thermo_fisher_instance = AdvisoryThermoFisher.from_json(json)
# print the JSON string representation of the object
print(AdvisoryThermoFisher.to_json())

# convert the object into a dict
advisory_thermo_fisher_dict = advisory_thermo_fisher_instance.to_dict()
# create an instance of AdvisoryThermoFisher from a dict
advisory_thermo_fisher_from_dict = AdvisoryThermoFisher.from_dict(advisory_thermo_fisher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


