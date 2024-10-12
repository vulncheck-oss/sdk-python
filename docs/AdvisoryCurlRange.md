# AdvisoryCurlRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[Dict[str, str]]** |  | [optional] 
**repo** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_curl_range import AdvisoryCurlRange

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCurlRange from a JSON string
advisory_curl_range_instance = AdvisoryCurlRange.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCurlRange.to_json())

# convert the object into a dict
advisory_curl_range_dict = advisory_curl_range_instance.to_dict()
# create an instance of AdvisoryCurlRange from a dict
advisory_curl_range_from_dict = AdvisoryCurlRange.from_dict(advisory_curl_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


