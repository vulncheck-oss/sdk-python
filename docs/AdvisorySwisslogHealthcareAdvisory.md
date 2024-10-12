# AdvisorySwisslogHealthcareAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_components** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_swisslog_healthcare_advisory import AdvisorySwisslogHealthcareAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySwisslogHealthcareAdvisory from a JSON string
advisory_swisslog_healthcare_advisory_instance = AdvisorySwisslogHealthcareAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySwisslogHealthcareAdvisory.to_json())

# convert the object into a dict
advisory_swisslog_healthcare_advisory_dict = advisory_swisslog_healthcare_advisory_instance.to_dict()
# create an instance of AdvisorySwisslogHealthcareAdvisory from a dict
advisory_swisslog_healthcare_advisory_from_dict = AdvisorySwisslogHealthcareAdvisory.from_dict(advisory_swisslog_healthcare_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


