# AdvisoryMokshaAdvisory

advisory.MokshaAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cve_ref** | [**AdvisoryMitreCVEListV5Ref**](AdvisoryMitreCVEListV5Ref.md) |  | [optional] 
**cvss3_score** | **float** |  | [optional] 
**cvss3_severity** | **str** |  | [optional] 
**cvss4_score** | **float** |  | [optional] 
**cvss4_severity** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**gcve** | **str** |  | [optional] 
**moksha_id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_moksha_advisory import AdvisoryMokshaAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMokshaAdvisory from a JSON string
advisory_moksha_advisory_instance = AdvisoryMokshaAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMokshaAdvisory.to_json())

# convert the object into a dict
advisory_moksha_advisory_dict = advisory_moksha_advisory_instance.to_dict()
# create an instance of AdvisoryMokshaAdvisory from a dict
advisory_moksha_advisory_from_dict = AdvisoryMokshaAdvisory.from_dict(advisory_moksha_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


