# AdvisoryGenetec


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
from vulncheck_sdk.models.advisory_genetec import AdvisoryGenetec

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGenetec from a JSON string
advisory_genetec_instance = AdvisoryGenetec.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGenetec.to_json())

# convert the object into a dict
advisory_genetec_dict = advisory_genetec_instance.to_dict()
# create an instance of AdvisoryGenetec from a dict
advisory_genetec_from_dict = AdvisoryGenetec.from_dict(advisory_genetec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


