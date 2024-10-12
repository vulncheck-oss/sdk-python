# ApiReferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_data** | [**List[ApiReferenceData]**](ApiReferenceData.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_references import ApiReferences

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReferences from a JSON string
api_references_instance = ApiReferences.from_json(json)
# print the JSON string representation of the object
print(ApiReferences.to_json())

# convert the object into a dict
api_references_dict = api_references_instance.to_dict()
# create an instance of ApiReferences from a dict
api_references_from_dict = ApiReferences.from_dict(api_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


