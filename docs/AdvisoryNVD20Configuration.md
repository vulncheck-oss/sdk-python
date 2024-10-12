# AdvisoryNVD20Configuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**negate** | **bool** |  | [optional] 
**nodes** | [**List[AdvisoryNVD20Node]**](AdvisoryNVD20Node.md) |  | [optional] 
**operator** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nvd20_configuration import AdvisoryNVD20Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNVD20Configuration from a JSON string
advisory_nvd20_configuration_instance = AdvisoryNVD20Configuration.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNVD20Configuration.to_json())

# convert the object into a dict
advisory_nvd20_configuration_dict = advisory_nvd20_configuration_instance.to_dict()
# create an instance of AdvisoryNVD20Configuration from a dict
advisory_nvd20_configuration_from_dict = AdvisoryNVD20Configuration.from_dict(advisory_nvd20_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


