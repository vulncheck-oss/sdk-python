# ApiDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description_data** | [**List[ApiDescriptionData]**](ApiDescriptionData.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_description import ApiDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDescription from a JSON string
api_description_instance = ApiDescription.from_json(json)
# print the JSON string representation of the object
print(ApiDescription.to_json())

# convert the object into a dict
api_description_dict = api_description_instance.to_dict()
# create an instance of ApiDescription from a dict
api_description_from_dict = ApiDescription.from_dict(api_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


