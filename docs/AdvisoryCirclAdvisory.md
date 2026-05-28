# AdvisoryCirclAdvisory

advisory.CirclAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circl_ref** | [**AdvisoryCirclRef**](AdvisoryCirclRef.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**gcve** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_circl_advisory import AdvisoryCirclAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCirclAdvisory from a JSON string
advisory_circl_advisory_instance = AdvisoryCirclAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCirclAdvisory.to_json())

# convert the object into a dict
advisory_circl_advisory_dict = advisory_circl_advisory_instance.to_dict()
# create an instance of AdvisoryCirclAdvisory from a dict
advisory_circl_advisory_from_dict = AdvisoryCirclAdvisory.from_dict(advisory_circl_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


