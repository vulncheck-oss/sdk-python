# AdvisoryCurl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**info** | [**AdvisoryOCurl**](AdvisoryOCurl.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_curl import AdvisoryCurl

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCurl from a JSON string
advisory_curl_instance = AdvisoryCurl.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCurl.to_json())

# convert the object into a dict
advisory_curl_dict = advisory_curl_instance.to_dict()
# create an instance of AdvisoryCurl from a dict
advisory_curl_from_dict = AdvisoryCurl.from_dict(advisory_curl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


