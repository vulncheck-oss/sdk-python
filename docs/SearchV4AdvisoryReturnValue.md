# SearchV4AdvisoryReturnValue

search.V4AdvisoryReturnValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**SearchV4AdvisoryMeta**](SearchV4AdvisoryMeta.md) |  | [optional] 
**data** | [**List[AdvisoryMitreCVEListV5Ref]**](AdvisoryMitreCVEListV5Ref.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.search_v4_advisory_return_value import SearchV4AdvisoryReturnValue

# TODO update the JSON string below
json = "{}"
# create an instance of SearchV4AdvisoryReturnValue from a JSON string
search_v4_advisory_return_value_instance = SearchV4AdvisoryReturnValue.from_json(json)
# print the JSON string representation of the object
print(SearchV4AdvisoryReturnValue.to_json())

# convert the object into a dict
search_v4_advisory_return_value_dict = search_v4_advisory_return_value_instance.to_dict()
# create an instance of SearchV4AdvisoryReturnValue from a dict
search_v4_advisory_return_value_from_dict = SearchV4AdvisoryReturnValue.from_dict(search_v4_advisory_return_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


