# AdvisorySiemensAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf_url** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvrf_url** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_update** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**ssa** | [**AdvisorySSASource**](AdvisorySSASource.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**txt_url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_advisory import AdvisorySiemensAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensAdvisory from a JSON string
advisory_siemens_advisory_instance = AdvisorySiemensAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensAdvisory.to_json())

# convert the object into a dict
advisory_siemens_advisory_dict = advisory_siemens_advisory_instance.to_dict()
# create an instance of AdvisorySiemensAdvisory from a dict
advisory_siemens_advisory_from_dict = AdvisorySiemensAdvisory.from_dict(advisory_siemens_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


