# ApiPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**name** | **str** | sort | [optional] 
**release** | **str** |  | [optional] 
**src** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_package import ApiPackage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPackage from a JSON string
api_package_instance = ApiPackage.from_json(json)
# print the JSON string representation of the object
print(ApiPackage.to_json())

# convert the object into a dict
api_package_dict = api_package_instance.to_dict()
# create an instance of ApiPackage from a dict
api_package_from_dict = ApiPackage.from_dict(api_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


