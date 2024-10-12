# V3controllersPurlResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purl_struct** | [**PurlPackageURLJSON**](PurlPackageURLJSON.md) | meta-data about the purl | [optional] 
**timestamp** | **str** | time of the transaction | [optional] 
**total_documents** | **int** | number of results found | [optional] 

## Example

```python
from vulncheck_sdk.models.v3controllers_purl_response_metadata import V3controllersPurlResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of V3controllersPurlResponseMetadata from a JSON string
v3controllers_purl_response_metadata_instance = V3controllersPurlResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(V3controllersPurlResponseMetadata.to_json())

# convert the object into a dict
v3controllers_purl_response_metadata_dict = v3controllers_purl_response_metadata_instance.to_dict()
# create an instance of V3controllersPurlResponseMetadata from a dict
v3controllers_purl_response_metadata_from_dict = V3controllersPurlResponseMetadata.from_dict(v3controllers_purl_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


