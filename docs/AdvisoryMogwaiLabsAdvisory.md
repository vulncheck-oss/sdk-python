# AdvisoryMogwaiLabsAdvisory

advisory.MogwaiLabsAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_version** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fixed_version** | **str** |  | [optional] 
**gcve** | **str** | From detail page | [optional] 
**id** | **str** | From index table | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mogwai_labs_advisory import AdvisoryMogwaiLabsAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMogwaiLabsAdvisory from a JSON string
advisory_mogwai_labs_advisory_instance = AdvisoryMogwaiLabsAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMogwaiLabsAdvisory.to_json())

# convert the object into a dict
advisory_mogwai_labs_advisory_dict = advisory_mogwai_labs_advisory_instance.to_dict()
# create an instance of AdvisoryMogwaiLabsAdvisory from a dict
advisory_mogwai_labs_advisory_from_dict = AdvisoryMogwaiLabsAdvisory.from_dict(advisory_mogwai_labs_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


