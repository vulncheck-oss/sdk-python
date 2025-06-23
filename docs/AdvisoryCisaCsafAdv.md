# AdvisoryCisaCsafAdv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf_json** | [**AdvisoryCSAF**](AdvisoryCSAF.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cisa_csaf_adv import AdvisoryCisaCsafAdv

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCisaCsafAdv from a JSON string
advisory_cisa_csaf_adv_instance = AdvisoryCisaCsafAdv.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCisaCsafAdv.to_json())

# convert the object into a dict
advisory_cisa_csaf_adv_dict = advisory_cisa_csaf_adv_instance.to_dict()
# create an instance of AdvisoryCisaCsafAdv from a dict
advisory_cisa_csaf_adv_from_dict = AdvisoryCisaCsafAdv.from_dict(advisory_cisa_csaf_adv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


