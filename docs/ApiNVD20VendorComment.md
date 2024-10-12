# ApiNVD20VendorComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_vendor_comment import ApiNVD20VendorComment

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20VendorComment from a JSON string
api_nvd20_vendor_comment_instance = ApiNVD20VendorComment.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20VendorComment.to_json())

# convert the object into a dict
api_nvd20_vendor_comment_dict = api_nvd20_vendor_comment_instance.to_dict()
# create an instance of ApiNVD20VendorComment from a dict
api_nvd20_vendor_comment_from_dict = ApiNVD20VendorComment.from_dict(api_nvd20_vendor_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


