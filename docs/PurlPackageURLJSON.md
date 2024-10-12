# PurlPackageURLJSON


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**qualifiers** | [**List[PurlQualifierJSON]**](PurlQualifierJSON.md) |  | [optional] 
**subpath** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.purl_package_urljson import PurlPackageURLJSON

# TODO update the JSON string below
json = "{}"
# create an instance of PurlPackageURLJSON from a JSON string
purl_package_urljson_instance = PurlPackageURLJSON.from_json(json)
# print the JSON string representation of the object
print(PurlPackageURLJSON.to_json())

# convert the object into a dict
purl_package_urljson_dict = purl_package_urljson_instance.to_dict()
# create an instance of PurlPackageURLJSON from a dict
purl_package_urljson_from_dict = PurlPackageURLJSON.from_dict(purl_package_urljson_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


