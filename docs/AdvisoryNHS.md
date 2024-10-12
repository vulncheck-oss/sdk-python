# AdvisoryNHS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**threat_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nhs import AdvisoryNHS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNHS from a JSON string
advisory_nhs_instance = AdvisoryNHS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNHS.to_json())

# convert the object into a dict
advisory_nhs_dict = advisory_nhs_instance.to_dict()
# create an instance of AdvisoryNHS from a dict
advisory_nhs_from_dict = AdvisoryNHS.from_dict(advisory_nhs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


