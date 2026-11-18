# NvdcpematchNvdMatchString

nvdcpematch.NvdMatchString

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_last_modified** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**criteria** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**match_criteria_id** | **str** |  | [optional] 
**matches** | [**List[NvdcpematchNvdCpeName]**](NvdcpematchNvdCpeName.md) |  | [optional] 
**status** | **str** |  | [optional] 
**version_end_excluding** | **str** |  | [optional] 
**version_end_including** | **str** |  | [optional] 
**version_start_excluding** | **str** |  | [optional] 
**version_start_including** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.nvdcpematch_nvd_match_string import NvdcpematchNvdMatchString

# TODO update the JSON string below
json = "{}"
# create an instance of NvdcpematchNvdMatchString from a JSON string
nvdcpematch_nvd_match_string_instance = NvdcpematchNvdMatchString.from_json(json)
# print the JSON string representation of the object
print(NvdcpematchNvdMatchString.to_json())

# convert the object into a dict
nvdcpematch_nvd_match_string_dict = nvdcpematch_nvd_match_string_instance.to_dict()
# create an instance of NvdcpematchNvdMatchString from a dict
nvdcpematch_nvd_match_string_from_dict = NvdcpematchNvdMatchString.from_dict(nvdcpematch_nvd_match_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


