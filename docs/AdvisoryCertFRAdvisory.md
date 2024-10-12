# AdvisoryCertFRAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_systems_fr** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**resume_fr** | **str** |  | [optional] 
**risks_fr** | **str** |  | [optional] 
**solution_fr** | **str** |  | [optional] 
**source_fr** | **str** |  | [optional] 
**title_fr** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cert_fr_advisory import AdvisoryCertFRAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCertFRAdvisory from a JSON string
advisory_cert_fr_advisory_instance = AdvisoryCertFRAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCertFRAdvisory.to_json())

# convert the object into a dict
advisory_cert_fr_advisory_dict = advisory_cert_fr_advisory_instance.to_dict()
# create an instance of AdvisoryCertFRAdvisory from a dict
advisory_cert_fr_advisory_from_dict = AdvisoryCertFRAdvisory.from_dict(advisory_cert_fr_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


