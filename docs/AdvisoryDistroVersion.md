# AdvisoryDistroVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | [optional] 
**published_date** | **str** |  | [optional] 
**release** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_distro_version import AdvisoryDistroVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDistroVersion from a JSON string
advisory_distro_version_instance = AdvisoryDistroVersion.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDistroVersion.to_json())

# convert the object into a dict
advisory_distro_version_dict = advisory_distro_version_instance.to_dict()
# create an instance of AdvisoryDistroVersion from a dict
advisory_distro_version_from_dict = AdvisoryDistroVersion.from_dict(advisory_distro_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


