# AdvisoryVDEAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf_json** | [**AdvisoryCSAF**](AdvisoryCSAF.md) |  | [optional] 
**csaf_url** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_revised** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vde** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vde_advisory import AdvisoryVDEAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVDEAdvisory from a JSON string
advisory_vde_advisory_instance = AdvisoryVDEAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVDEAdvisory.to_json())

# convert the object into a dict
advisory_vde_advisory_dict = advisory_vde_advisory_instance.to_dict()
# create an instance of AdvisoryVDEAdvisory from a dict
advisory_vde_advisory_from_dict = AdvisoryVDEAdvisory.from_dict(advisory_vde_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


