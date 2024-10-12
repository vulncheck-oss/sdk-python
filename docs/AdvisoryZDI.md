# AdvisoryZDI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cves** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**cvss_version** | **str** |  | [optional] 
**discoverers** | **List[str]** |  | [optional] 
**filter_ids_dv** | **List[str]** |  | [optional] 
**last_updated_at** | **str** |  | [optional] 
**products** | [**List[AdvisoryZDIProduct]**](AdvisoryZDIProduct.md) |  | [optional] 
**public_advisory** | **str** |  | [optional] 
**published_date** | **str** |  | [optional] 
**responses** | [**List[AdvisoryZDIResponse]**](AdvisoryZDIResponse.md) |  | [optional] 
**title** | **str** |  | [optional] 
**zdi_can** | **str** |  | [optional] 
**zdi_public** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zdi import AdvisoryZDI

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZDI from a JSON string
advisory_zdi_instance = AdvisoryZDI.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZDI.to_json())

# convert the object into a dict
advisory_zdi_dict = advisory_zdi_instance.to_dict()
# create an instance of AdvisoryZDI from a dict
advisory_zdi_from_dict = AdvisoryZDI.from_dict(advisory_zdi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


