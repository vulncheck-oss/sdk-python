# AdvisoryMProviderMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_updated** | **str** | FIXME: flip to time | [optional] 
**org_id** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_provider_metadata import AdvisoryMProviderMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMProviderMetadata from a JSON string
advisory_m_provider_metadata_instance = AdvisoryMProviderMetadata.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMProviderMetadata.to_json())

# convert the object into a dict
advisory_m_provider_metadata_dict = advisory_m_provider_metadata_instance.to_dict()
# create an instance of AdvisoryMProviderMetadata from a dict
advisory_m_provider_metadata_from_dict = AdvisoryMProviderMetadata.from_dict(advisory_m_provider_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


