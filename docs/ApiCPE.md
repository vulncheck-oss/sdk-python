# ApiCPE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edition** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**other** | **str** |  | [optional] 
**part** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**sw_edition** | **str** |  | [optional] 
**target_hw** | **str** |  | [optional] 
**target_sw** | **str** |  | [optional] 
**update** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cpe import ApiCPE

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCPE from a JSON string
api_cpe_instance = ApiCPE.from_json(json)
# print the JSON string representation of the object
print(ApiCPE.to_json())

# convert the object into a dict
api_cpe_dict = api_cpe_instance.to_dict()
# create an instance of ApiCPE from a dict
api_cpe_from_dict = ApiCPE.from_dict(api_cpe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


