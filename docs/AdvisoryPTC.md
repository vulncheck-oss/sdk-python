# AdvisoryPTC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ptc import AdvisoryPTC

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPTC from a JSON string
advisory_ptc_instance = AdvisoryPTC.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPTC.to_json())

# convert the object into a dict
advisory_ptc_dict = advisory_ptc_instance.to_dict()
# create an instance of AdvisoryPTC from a dict
advisory_ptc_from_dict = AdvisoryPTC.from_dict(advisory_ptc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


