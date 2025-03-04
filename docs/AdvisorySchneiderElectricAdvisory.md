# AdvisorySchneiderElectricAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf_url** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**pdf_url** | **str** |  | [optional] 
**schneider_cves** | [**List[AdvisorySchneiderCVE]**](AdvisorySchneiderCVE.md) |  | [optional] 
**schneider_electric_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_schneider_electric_advisory import AdvisorySchneiderElectricAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySchneiderElectricAdvisory from a JSON string
advisory_schneider_electric_advisory_instance = AdvisorySchneiderElectricAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySchneiderElectricAdvisory.to_json())

# convert the object into a dict
advisory_schneider_electric_advisory_dict = advisory_schneider_electric_advisory_instance.to_dict()
# create an instance of AdvisorySchneiderElectricAdvisory from a dict
advisory_schneider_electric_advisory_from_dict = AdvisorySchneiderElectricAdvisory.from_dict(advisory_schneider_electric_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


