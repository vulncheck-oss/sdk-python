# AdvisoryOCurl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryCurlAffected]**](AdvisoryCurlAffected.md) |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**credits** | [**List[AdvisoryCurlCredit]**](AdvisoryCurlCredit.md) |  | [optional] 
**database_specific** | [**AdvisoryDBSpecific**](AdvisoryDBSpecific.md) |  | [optional] 
**details** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**schema_version** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_o_curl import AdvisoryOCurl

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOCurl from a JSON string
advisory_o_curl_instance = AdvisoryOCurl.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOCurl.to_json())

# convert the object into a dict
advisory_o_curl_dict = advisory_o_curl_instance.to_dict()
# create an instance of AdvisoryOCurl from a dict
advisory_o_curl_from_dict = AdvisoryOCurl.from_dict(advisory_o_curl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


