# AdvisoryQNAPAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**last_update_date** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**severity_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_qnap_advisory import AdvisoryQNAPAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryQNAPAdvisory from a JSON string
advisory_qnap_advisory_instance = AdvisoryQNAPAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryQNAPAdvisory.to_json())

# convert the object into a dict
advisory_qnap_advisory_dict = advisory_qnap_advisory_instance.to_dict()
# create an instance of AdvisoryQNAPAdvisory from a dict
advisory_qnap_advisory_from_dict = AdvisoryQNAPAdvisory.from_dict(advisory_qnap_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


