# AdvisoryEmersonAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**emerson_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_emerson_advisory import AdvisoryEmersonAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEmersonAdvisory from a JSON string
advisory_emerson_advisory_instance = AdvisoryEmersonAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEmersonAdvisory.to_json())

# convert the object into a dict
advisory_emerson_advisory_dict = advisory_emerson_advisory_instance.to_dict()
# create an instance of AdvisoryEmersonAdvisory from a dict
advisory_emerson_advisory_from_dict = AdvisoryEmersonAdvisory.from_dict(advisory_emerson_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


