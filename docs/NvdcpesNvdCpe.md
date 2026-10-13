# NvdcpesNvdCpe

nvdcpes.NvdCpe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_name** | **str** |  | [optional] 
**cpe_name_id** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**deprecated_by** | [**List[NvdcpesNvdCpeDeprecation]**](NvdcpesNvdCpeDeprecation.md) |  | [optional] 
**deprecates** | [**List[NvdcpesNvdCpeDeprecation]**](NvdcpesNvdCpeDeprecation.md) |  | [optional] 
**last_modified** | **str** |  | [optional] 
**refs** | [**List[NvdcpesNvdCpeReference]**](NvdcpesNvdCpeReference.md) |  | [optional] 
**titles** | [**List[NvdcpesNvdCpeTitle]**](NvdcpesNvdCpeTitle.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.nvdcpes_nvd_cpe import NvdcpesNvdCpe

# TODO update the JSON string below
json = "{}"
# create an instance of NvdcpesNvdCpe from a JSON string
nvdcpes_nvd_cpe_instance = NvdcpesNvdCpe.from_json(json)
# print the JSON string representation of the object
print(NvdcpesNvdCpe.to_json())

# convert the object into a dict
nvdcpes_nvd_cpe_dict = nvdcpes_nvd_cpe_instance.to_dict()
# create an instance of NvdcpesNvdCpe from a dict
nvdcpes_nvd_cpe_from_dict = NvdcpesNvdCpe.from_dict(nvdcpes_nvd_cpe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


