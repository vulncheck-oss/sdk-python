# AdvisorySpacelabsHealthcareAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_spacelabs_healthcare_advisory import AdvisorySpacelabsHealthcareAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySpacelabsHealthcareAdvisory from a JSON string
advisory_spacelabs_healthcare_advisory_instance = AdvisorySpacelabsHealthcareAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySpacelabsHealthcareAdvisory.to_json())

# convert the object into a dict
advisory_spacelabs_healthcare_advisory_dict = advisory_spacelabs_healthcare_advisory_instance.to_dict()
# create an instance of AdvisorySpacelabsHealthcareAdvisory from a dict
advisory_spacelabs_healthcare_advisory_from_dict = AdvisorySpacelabsHealthcareAdvisory.from_dict(advisory_spacelabs_healthcare_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


