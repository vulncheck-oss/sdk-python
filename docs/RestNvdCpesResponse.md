# RestNvdCpesResponse

rest.NvdCpesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 
**next_cursor** | **str** | Present only when the request sent &#x60;cursor&#x60; and a further page exists. | [optional] 
**products** | [**List[NvdcpesNvdCpeEnvelopeEntry]**](NvdcpesNvdCpeEnvelopeEntry.md) |  | 
**results_per_page** | **int** |  | 
**start_index** | **int** |  | 
**timestamp** | **str** |  | 
**total_results** | **int** |  | 
**version** | **str** |  | 

## Example

```python
from vulncheck_sdk.models.rest_nvd_cpes_response import RestNvdCpesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestNvdCpesResponse from a JSON string
rest_nvd_cpes_response_instance = RestNvdCpesResponse.from_json(json)
# print the JSON string representation of the object
print(RestNvdCpesResponse.to_json())

# convert the object into a dict
rest_nvd_cpes_response_dict = rest_nvd_cpes_response_instance.to_dict()
# create an instance of RestNvdCpesResponse from a dict
rest_nvd_cpes_response_from_dict = RestNvdCpesResponse.from_dict(rest_nvd_cpes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


