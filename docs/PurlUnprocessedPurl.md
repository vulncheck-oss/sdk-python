# PurlUnprocessedPurl

purl.UnprocessedPurl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purl** | **str** | The purl exactly as submitted. | [optional] 
**reason** | **str** | Why this purl was not looked up. One of: \&quot;unsupported_type\&quot; (a valid purl for an ecosystem VulnCheck does not index), \&quot;unparseable\&quot; (not a valid purl), \&quot;unsupported_distro\&quot; (a distro-scoped purl whose distro qualifier is missing or unrecognised, e.g. pkg:deb/debian/curl with no distro&#x3D;). Treat this as an open set: further values may be added. | [optional] 

## Example

```python
from vulncheck_sdk.models.purl_unprocessed_purl import PurlUnprocessedPurl

# TODO update the JSON string below
json = "{}"
# create an instance of PurlUnprocessedPurl from a JSON string
purl_unprocessed_purl_instance = PurlUnprocessedPurl.from_json(json)
# print the JSON string representation of the object
print(PurlUnprocessedPurl.to_json())

# convert the object into a dict
purl_unprocessed_purl_dict = purl_unprocessed_purl_instance.to_dict()
# create an instance of PurlUnprocessedPurl from a dict
purl_unprocessed_purl_from_dict = PurlUnprocessedPurl.from_dict(purl_unprocessed_purl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


