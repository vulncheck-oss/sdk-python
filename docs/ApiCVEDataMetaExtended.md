# ApiCVEDataMetaExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**assigner** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cve_data_meta_extended import ApiCVEDataMetaExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCVEDataMetaExtended from a JSON string
api_cve_data_meta_extended_instance = ApiCVEDataMetaExtended.from_json(json)
# print the JSON string representation of the object
print(ApiCVEDataMetaExtended.to_json())

# convert the object into a dict
api_cve_data_meta_extended_dict = api_cve_data_meta_extended_instance.to_dict()
# create an instance of ApiCVEDataMetaExtended from a dict
api_cve_data_meta_extended_from_dict = ApiCVEDataMetaExtended.from_dict(api_cve_data_meta_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


