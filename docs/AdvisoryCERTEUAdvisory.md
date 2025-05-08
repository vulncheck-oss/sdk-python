# AdvisoryCERTEUAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**affected_products** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**history** | **List[str]** |  | [optional] 
**link** | **str** |  | [optional] 
**recommendations** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**technical_details** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_certeu_advisory import AdvisoryCERTEUAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCERTEUAdvisory from a JSON string
advisory_certeu_advisory_instance = AdvisoryCERTEUAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCERTEUAdvisory.to_json())

# convert the object into a dict
advisory_certeu_advisory_dict = advisory_certeu_advisory_instance.to_dict()
# create an instance of AdvisoryCERTEUAdvisory from a dict
advisory_certeu_advisory_from_dict = AdvisoryCERTEUAdvisory.from_dict(advisory_certeu_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


