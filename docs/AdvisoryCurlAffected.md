# AdvisoryCurlAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**List[AdvisoryCurlRange]**](AdvisoryCurlRange.md) |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_curl_affected import AdvisoryCurlAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCurlAffected from a JSON string
advisory_curl_affected_instance = AdvisoryCurlAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCurlAffected.to_json())

# convert the object into a dict
advisory_curl_affected_dict = advisory_curl_affected_instance.to_dict()
# create an instance of AdvisoryCurlAffected from a dict
advisory_curl_affected_from_dict = AdvisoryCurlAffected.from_dict(advisory_curl_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


