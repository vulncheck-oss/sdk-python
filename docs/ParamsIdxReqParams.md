# ParamsIdxReqParams

model representing the parameters to constrain the vulnerability search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Specify an Alias to search with | [optional] 
**asn** | **str** | IpIntel Only: Specify an ASN to search with | [optional] 
**botnet_name** | **str** | Specify a Botnet Name to search with | [optional] 
**cidr** | **str** | IpIntel Only: Specify a IPv4 or IPv6 cidr to search with | [optional] 
**country** | **str** | IpIntel Only: Specify a country name to search with | [optional] 
**country_code** | **str** | IpIntel Only: Specify a country code to search with | [optional] 
**cve** | **str** | Specify one or more CVEs (comma delimited) to search with. | [optional] 
**hostname** | **str** | IpIntel Only: Specify a string to search in the list of hostnames | [optional] 
**iava** | **str** | Specify an IAVA to search with | [optional] 
**jvndb** | **str** | Specify a JVNDB ID to search with | [optional] 
**limit** | **str** | Limit the number of documents returned | [optional] 
**matches** | **str** | IpIntel Only: Specify a string to search in the matches field | [optional] 
**misp_id** | **str** | Specify a MISP ID to search with | [optional] 
**mitre_id** | **str** | Specify a MITRE ID to search with | [optional] 
**order** | **str** | Return results in ascending or descending order | [optional] 
**published** | **str** | Specify a published date to search with | [optional] 
**published_end** | **str** | Specify an ending published date to filter with | [optional] 
**published_start** | **str** | Specify a starting published date to filter with | [optional] 
**ransomware_family_name** | **str** | Specify a Ransomware Family Name to search with | [optional] 
**sort** | **str** | Return results sorted by field | [optional] 
**threat_actor_name** | **str** | Specify a Threat Actor Name to search with | [optional] 
**type_id** | **str** | IpIntel Only: Choices are c2 or initial-access | [optional] 
**type_kind** | **str** | IpIntel Only: Filter results by &#39;type.kind&#39; | [optional] 
**updated_end** | **str** | Specify an ending last modified date to filter with | [optional] 
**updated_start** | **str** | Specify a starting last modified date to filter with | [optional] 

## Example

```python
from vulncheck_sdk.models.params_idx_req_params import ParamsIdxReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of ParamsIdxReqParams from a JSON string
params_idx_req_params_instance = ParamsIdxReqParams.from_json(json)
# print the JSON string representation of the object
print(ParamsIdxReqParams.to_json())

# convert the object into a dict
params_idx_req_params_dict = params_idx_req_params_instance.to_dict()
# create an instance of ParamsIdxReqParams from a dict
params_idx_req_params_from_dict = ParamsIdxReqParams.from_dict(params_idx_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


