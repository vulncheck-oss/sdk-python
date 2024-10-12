# ApiCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_data_meta** | [**ApiCVEDataMeta**](ApiCVEDataMeta.md) |  | [optional] 
**data_format** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 
**description** | [**ApiDescription**](ApiDescription.md) |  | [optional] 
**problemtype** | [**ApiProblemType**](ApiProblemType.md) |  | [optional] 
**references** | [**ApiReferences**](ApiReferences.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cve import ApiCVE

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCVE from a JSON string
api_cve_instance = ApiCVE.from_json(json)
# print the JSON string representation of the object
print(ApiCVE.to_json())

# convert the object into a dict
api_cve_dict = api_cve_instance.to_dict()
# create an instance of ApiCVE from a dict
api_cve_from_dict = ApiCVE.from_dict(api_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


