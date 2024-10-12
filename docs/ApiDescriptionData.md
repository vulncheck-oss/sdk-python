# ApiDescriptionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_description_data import ApiDescriptionData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDescriptionData from a JSON string
api_description_data_instance = ApiDescriptionData.from_json(json)
# print the JSON string representation of the object
print(ApiDescriptionData.to_json())

# convert the object into a dict
api_description_data_dict = api_description_data_instance.to_dict()
# create an instance of ApiDescriptionData from a dict
api_description_data_from_dict = ApiDescriptionData.from_dict(api_description_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


