# AdvisoryMitsubishiElectricAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_revised** | **str** | could nuke this at some pt in the future as it&#39;s a dupe | [optional] 
**mitsubishi_electric_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mitsubishi_electric_advisory import AdvisoryMitsubishiElectricAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMitsubishiElectricAdvisory from a JSON string
advisory_mitsubishi_electric_advisory_instance = AdvisoryMitsubishiElectricAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMitsubishiElectricAdvisory.to_json())

# convert the object into a dict
advisory_mitsubishi_electric_advisory_dict = advisory_mitsubishi_electric_advisory_instance.to_dict()
# create an instance of AdvisoryMitsubishiElectricAdvisory from a dict
advisory_mitsubishi_electric_advisory_from_dict = AdvisoryMitsubishiElectricAdvisory.from_dict(advisory_mitsubishi_electric_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


