# V3controllersPurlsResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** | time of the transaction | [optional] 
**total_documents** | **int** | number of results found | [optional] 

## Example

```python
from vulncheck_sdk.models.v3controllers_purls_response_metadata import V3controllersPurlsResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of V3controllersPurlsResponseMetadata from a JSON string
v3controllers_purls_response_metadata_instance = V3controllersPurlsResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(V3controllersPurlsResponseMetadata.to_json())

# convert the object into a dict
v3controllers_purls_response_metadata_dict = v3controllers_purls_response_metadata_instance.to_dict()
# create an instance of V3controllersPurlsResponseMetadata from a dict
v3controllers_purls_response_metadata_from_dict = V3controllersPurlsResponseMetadata.from_dict(v3controllers_purls_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


