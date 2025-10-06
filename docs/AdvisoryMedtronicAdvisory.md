# AdvisoryMedtronicAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_medtronic_advisory import AdvisoryMedtronicAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMedtronicAdvisory from a JSON string
advisory_medtronic_advisory_instance = AdvisoryMedtronicAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMedtronicAdvisory.to_json())

# convert the object into a dict
advisory_medtronic_advisory_dict = advisory_medtronic_advisory_instance.to_dict()
# create an instance of AdvisoryMedtronicAdvisory from a dict
advisory_medtronic_advisory_from_dict = AdvisoryMedtronicAdvisory.from_dict(advisory_medtronic_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


