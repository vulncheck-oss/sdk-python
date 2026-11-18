# RestNvdSourceResponse

rest.NvdSourceResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 
**results_per_page** | **int** |  | 
**sources** | [**List[NvdsourceNvdSource]**](NvdsourceNvdSource.md) |  | 
**start_index** | **int** |  | 
**timestamp** | **str** |  | 
**total_results** | **int** |  | 
**version** | **str** |  | 

## Example

```python
from vulncheck_sdk.models.rest_nvd_source_response import RestNvdSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestNvdSourceResponse from a JSON string
rest_nvd_source_response_instance = RestNvdSourceResponse.from_json(json)
# print the JSON string representation of the object
print(RestNvdSourceResponse.to_json())

# convert the object into a dict
rest_nvd_source_response_dict = rest_nvd_source_response_instance.to_dict()
# create an instance of RestNvdSourceResponse from a dict
rest_nvd_source_response_from_dict = RestNvdSourceResponse.from_dict(rest_nvd_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


