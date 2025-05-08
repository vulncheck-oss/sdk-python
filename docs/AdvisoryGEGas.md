# AdvisoryGEGas


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
from vulncheck_sdk.models.advisory_ge_gas import AdvisoryGEGas

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGEGas from a JSON string
advisory_ge_gas_instance = AdvisoryGEGas.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGEGas.to_json())

# convert the object into a dict
advisory_ge_gas_dict = advisory_ge_gas_instance.to_dict()
# create an instance of AdvisoryGEGas from a dict
advisory_ge_gas_from_dict = AdvisoryGEGas.from_dict(advisory_ge_gas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


