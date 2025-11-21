# AdvisoryMicrosoftFileMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Full path (FilePath + FileName or FriendlyName) | [optional] 
**maximum_file_version** | **str** |  | [optional] 
**minimum_file_version** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**sha1_hash** | **str** |  | [optional] 
**sha256_hash** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_microsoft_file_metadata import AdvisoryMicrosoftFileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMicrosoftFileMetadata from a JSON string
advisory_microsoft_file_metadata_instance = AdvisoryMicrosoftFileMetadata.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMicrosoftFileMetadata.to_json())

# convert the object into a dict
advisory_microsoft_file_metadata_dict = advisory_microsoft_file_metadata_instance.to_dict()
# create an instance of AdvisoryMicrosoftFileMetadata from a dict
advisory_microsoft_file_metadata_from_dict = AdvisoryMicrosoftFileMetadata.from_dict(advisory_microsoft_file_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


