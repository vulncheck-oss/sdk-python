# AdvisoryTrustwave


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_trustwave import AdvisoryTrustwave

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTrustwave from a JSON string
advisory_trustwave_instance = AdvisoryTrustwave.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTrustwave.to_json())

# convert the object into a dict
advisory_trustwave_dict = advisory_trustwave_instance.to_dict()
# create an instance of AdvisoryTrustwave from a dict
advisory_trustwave_from_dict = AdvisoryTrustwave.from_dict(advisory_trustwave_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


