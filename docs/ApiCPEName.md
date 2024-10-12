# ApiCPEName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe22_uri** | **str** |  | [optional] 
**cpe23_uri** | **str** |  | [optional] 
**last_modified_date** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cpe_name import ApiCPEName

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCPEName from a JSON string
api_cpe_name_instance = ApiCPEName.from_json(json)
# print the JSON string representation of the object
print(ApiCPEName.to_json())

# convert the object into a dict
api_cpe_name_dict = api_cpe_name_instance.to_dict()
# create an instance of ApiCPEName from a dict
api_cpe_name_from_dict = ApiCPEName.from_dict(api_cpe_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


