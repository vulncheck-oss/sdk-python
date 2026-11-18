# RestNvdCveHistoryResponse

rest.NvdCveHistoryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_changes** | [**List[RestNvdChangeEnvelopeEntry]**](RestNvdChangeEnvelopeEntry.md) |  | 
**format** | **str** |  | 
**next_cursor** | **str** | Present only when the request sent &#x60;cursor&#x60; and a further page exists. | [optional] 
**results_per_page** | **int** |  | 
**start_index** | **int** |  | 
**timestamp** | **str** |  | 
**total_results** | **int** |  | 
**version** | **str** |  | 

## Example

```python
from vulncheck_sdk.models.rest_nvd_cve_history_response import RestNvdCveHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestNvdCveHistoryResponse from a JSON string
rest_nvd_cve_history_response_instance = RestNvdCveHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(RestNvdCveHistoryResponse.to_json())

# convert the object into a dict
rest_nvd_cve_history_response_dict = rest_nvd_cve_history_response_instance.to_dict()
# create an instance of RestNvdCveHistoryResponse from a dict
rest_nvd_cve_history_response_from_dict = RestNvdCveHistoryResponse.from_dict(rest_nvd_cve_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


