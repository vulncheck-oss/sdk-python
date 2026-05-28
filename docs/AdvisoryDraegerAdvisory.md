# AdvisoryDraegerAdvisory

advisory.DraegerAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor_id** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_draeger_advisory import AdvisoryDraegerAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDraegerAdvisory from a JSON string
advisory_draeger_advisory_instance = AdvisoryDraegerAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDraegerAdvisory.to_json())

# convert the object into a dict
advisory_draeger_advisory_dict = advisory_draeger_advisory_instance.to_dict()
# create an instance of AdvisoryDraegerAdvisory from a dict
advisory_draeger_advisory_from_dict = AdvisoryDraegerAdvisory.from_dict(advisory_draeger_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


