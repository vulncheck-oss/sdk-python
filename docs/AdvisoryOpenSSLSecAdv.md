# AdvisoryOpenSSLSecAdv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vulnerabilities** | [**List[AdvisoryOpenSSLVulnerability]**](AdvisoryOpenSSLVulnerability.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_open_ssl_sec_adv import AdvisoryOpenSSLSecAdv

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOpenSSLSecAdv from a JSON string
advisory_open_ssl_sec_adv_instance = AdvisoryOpenSSLSecAdv.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOpenSSLSecAdv.to_json())

# convert the object into a dict
advisory_open_ssl_sec_adv_dict = advisory_open_ssl_sec_adv_instance.to_dict()
# create an instance of AdvisoryOpenSSLSecAdv from a dict
advisory_open_ssl_sec_adv_from_dict = AdvisoryOpenSSLSecAdv.from_dict(advisory_open_ssl_sec_adv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


