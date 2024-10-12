# AdvisoryNEC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**nvd_id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nec import AdvisoryNEC

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNEC from a JSON string
advisory_nec_instance = AdvisoryNEC.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNEC.to_json())

# convert the object into a dict
advisory_nec_dict = advisory_nec_instance.to_dict()
# create an instance of AdvisoryNEC from a dict
advisory_nec_from_dict = AdvisoryNEC.from_dict(advisory_nec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


