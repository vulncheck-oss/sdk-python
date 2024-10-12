# AdvisoryDeltaAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**recommended_action** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_delta_advisory import AdvisoryDeltaAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDeltaAdvisory from a JSON string
advisory_delta_advisory_instance = AdvisoryDeltaAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDeltaAdvisory.to_json())

# convert the object into a dict
advisory_delta_advisory_dict = advisory_delta_advisory_instance.to_dict()
# create an instance of AdvisoryDeltaAdvisory from a dict
advisory_delta_advisory_from_dict = AdvisoryDeltaAdvisory.from_dict(advisory_delta_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


