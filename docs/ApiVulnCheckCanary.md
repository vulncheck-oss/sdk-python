# ApiVulnCheckCanary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**client_fingerprints** | [**ApiClientFingerprints**](ApiClientFingerprints.md) |  | [optional] 
**cve** | **str** |  | [optional] 
**dst_country** | **str** |  | [optional] 
**http** | [**ApiHTTPDetails**](ApiHTTPDetails.md) |  | [optional] 
**severity** | **int** |  | [optional] 
**signature** | **str** |  | [optional] 
**signature_id** | **int** |  | [optional] 
**src_country** | **str** |  | [optional] 
**src_ip** | **str** |  | [optional] 
**src_port** | **int** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_vuln_check_canary import ApiVulnCheckCanary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiVulnCheckCanary from a JSON string
api_vuln_check_canary_instance = ApiVulnCheckCanary.from_json(json)
# print the JSON string representation of the object
print(ApiVulnCheckCanary.to_json())

# convert the object into a dict
api_vuln_check_canary_dict = api_vuln_check_canary_instance.to_dict()
# create an instance of ApiVulnCheckCanary from a dict
api_vuln_check_canary_from_dict = ApiVulnCheckCanary.from_dict(api_vuln_check_canary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


