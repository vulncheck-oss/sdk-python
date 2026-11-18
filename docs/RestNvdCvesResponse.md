# RestNvdCvesResponse

rest.NvdCvesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 
**next_cursor** | **str** | Present only when the request sent &#x60;cursor&#x60; and a further page exists. | [optional] 
**results_per_page** | **int** |  | 
**start_index** | **int** |  | 
**timestamp** | **str** |  | 
**total_results** | **int** |  | 
**version** | **str** |  | 
**vulnerabilities** | [**List[NvdcvesNvdCveEnvelopeEntry]**](NvdcvesNvdCveEnvelopeEntry.md) |  | 

## Example

```python
from vulncheck_sdk.models.rest_nvd_cves_response import RestNvdCvesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestNvdCvesResponse from a JSON string
rest_nvd_cves_response_instance = RestNvdCvesResponse.from_json(json)
# print the JSON string representation of the object
print(RestNvdCvesResponse.to_json())

# convert the object into a dict
rest_nvd_cves_response_dict = rest_nvd_cves_response_instance.to_dict()
# create an instance of RestNvdCvesResponse from a dict
rest_nvd_cves_response_from_dict = RestNvdCvesResponse.from_dict(rest_nvd_cves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


