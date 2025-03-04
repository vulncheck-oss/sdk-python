# PurlsPurlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | **object** |  | [optional] 
**cves** | **List[str]** |  | [optional] 
**licenses** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**purl** | **List[str]** |  | [optional] 
**version** | **str** |  | [optional] 
**vulnerabilities** | [**List[PurlsVulnerability]**](PurlsVulnerability.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.purls_purl_response import PurlsPurlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PurlsPurlResponse from a JSON string
purls_purl_response_instance = PurlsPurlResponse.from_json(json)
# print the JSON string representation of the object
print(PurlsPurlResponse.to_json())

# convert the object into a dict
purls_purl_response_dict = purls_purl_response_instance.to_dict()
# create an instance of PurlsPurlResponse from a dict
purls_purl_response_from_dict = PurlsPurlResponse.from_dict(purls_purl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


