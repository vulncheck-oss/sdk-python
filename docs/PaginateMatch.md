# PaginateMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.paginate_match import PaginateMatch

# TODO update the JSON string below
json = "{}"
# create an instance of PaginateMatch from a JSON string
paginate_match_instance = PaginateMatch.from_json(json)
# print the JSON string representation of the object
print(PaginateMatch.to_json())

# convert the object into a dict
paginate_match_dict = paginate_match_instance.to_dict()
# create an instance of PaginateMatch from a dict
paginate_match_from_dict = PaginateMatch.from_dict(paginate_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


