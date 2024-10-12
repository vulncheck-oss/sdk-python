# AdvisoryBoschAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bosch_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_revised** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bosch_advisory import AdvisoryBoschAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBoschAdvisory from a JSON string
advisory_bosch_advisory_instance = AdvisoryBoschAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBoschAdvisory.to_json())

# convert the object into a dict
advisory_bosch_advisory_dict = advisory_bosch_advisory_instance.to_dict()
# create an instance of AdvisoryBoschAdvisory from a dict
advisory_bosch_advisory_from_dict = AdvisoryBoschAdvisory.from_dict(advisory_bosch_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


