# AdvisoryGEHealthcareAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_updated** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ge_healthcare_advisory import AdvisoryGEHealthcareAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGEHealthcareAdvisory from a JSON string
advisory_ge_healthcare_advisory_instance = AdvisoryGEHealthcareAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGEHealthcareAdvisory.to_json())

# convert the object into a dict
advisory_ge_healthcare_advisory_dict = advisory_ge_healthcare_advisory_instance.to_dict()
# create an instance of AdvisoryGEHealthcareAdvisory from a dict
advisory_ge_healthcare_advisory_from_dict = AdvisoryGEHealthcareAdvisory.from_dict(advisory_ge_healthcare_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


