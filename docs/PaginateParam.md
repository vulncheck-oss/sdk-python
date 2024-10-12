# PaginateParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filtering** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.paginate_param import PaginateParam

# TODO update the JSON string below
json = "{}"
# create an instance of PaginateParam from a JSON string
paginate_param_instance = PaginateParam.from_json(json)
# print the JSON string representation of the object
print(PaginateParam.to_json())

# convert the object into a dict
paginate_param_dict = paginate_param_instance.to_dict()
# create an instance of PaginateParam from a dict
paginate_param_from_dict = PaginateParam.from_dict(paginate_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


