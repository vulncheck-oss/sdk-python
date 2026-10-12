# ApiNVD20SsvcOption

api.NVD20SsvcOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatable** | **str** |  | [optional] 
**exploitation** | **str** |  | [optional] 
**technical_impact** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_ssvc_option import ApiNVD20SsvcOption

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20SsvcOption from a JSON string
api_nvd20_ssvc_option_instance = ApiNVD20SsvcOption.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20SsvcOption.to_json())

# convert the object into a dict
api_nvd20_ssvc_option_dict = api_nvd20_ssvc_option_instance.to_dict()
# create an instance of ApiNVD20SsvcOption from a dict
api_nvd20_ssvc_option_from_dict = ApiNVD20SsvcOption.from_dict(api_nvd20_ssvc_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


