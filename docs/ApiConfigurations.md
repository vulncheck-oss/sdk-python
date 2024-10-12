# ApiConfigurations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_data_version** | **str** |  | [optional] 
**nodes** | [**List[ApiNodes]**](ApiNodes.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_configurations import ApiConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigurations from a JSON string
api_configurations_instance = ApiConfigurations.from_json(json)
# print the JSON string representation of the object
print(ApiConfigurations.to_json())

# convert the object into a dict
api_configurations_dict = api_configurations_instance.to_dict()
# create an instance of ApiConfigurations from a dict
api_configurations_from_dict = ApiConfigurations.from_dict(api_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


