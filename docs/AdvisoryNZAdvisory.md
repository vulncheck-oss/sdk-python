# AdvisoryNZAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**happening** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**look_for** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**what_to_do** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nz_advisory import AdvisoryNZAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNZAdvisory from a JSON string
advisory_nz_advisory_instance = AdvisoryNZAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNZAdvisory.to_json())

# convert the object into a dict
advisory_nz_advisory_dict = advisory_nz_advisory_instance.to_dict()
# create an instance of AdvisoryNZAdvisory from a dict
advisory_nz_advisory_from_dict = AdvisoryNZAdvisory.from_dict(advisory_nz_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


