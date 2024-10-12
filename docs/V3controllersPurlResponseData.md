# V3controllersPurlResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cves** | **List[str]** | list of associated CVE &#39;s | [optional] 
**vulnerabilities** | [**List[ApiOSSPackageVulnerability]**](ApiOSSPackageVulnerability.md) | list of associated vulnerabilities | [optional] 

## Example

```python
from vulncheck_sdk.models.v3controllers_purl_response_data import V3controllersPurlResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of V3controllersPurlResponseData from a JSON string
v3controllers_purl_response_data_instance = V3controllersPurlResponseData.from_json(json)
# print the JSON string representation of the object
print(V3controllersPurlResponseData.to_json())

# convert the object into a dict
v3controllers_purl_response_data_dict = v3controllers_purl_response_data_instance.to_dict()
# create an instance of V3controllersPurlResponseData from a dict
v3controllers_purl_response_data_from_dict = V3controllersPurlResponseData.from_dict(v3controllers_purl_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


