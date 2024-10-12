# AdvisoryTWCertAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_cn** | **str** |  | [optional] 
**affected_en** | **str** |  | [optional] 
**credit_cn** | **str** |  | [optional] 
**credit_en** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description_cn** | **str** |  | [optional] 
**description_en** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**solution_cn** | **str** |  | [optional] 
**solution_en** | **str** |  | [optional] 
**title_cn** | **str** |  | [optional] 
**title_en** | **str** |  | [optional] 
**tvnid** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tw_cert_advisory import AdvisoryTWCertAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTWCertAdvisory from a JSON string
advisory_tw_cert_advisory_instance = AdvisoryTWCertAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTWCertAdvisory.to_json())

# convert the object into a dict
advisory_tw_cert_advisory_dict = advisory_tw_cert_advisory_instance.to_dict()
# create an instance of AdvisoryTWCertAdvisory from a dict
advisory_tw_cert_advisory_from_dict = AdvisoryTWCertAdvisory.from_dict(advisory_tw_cert_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


