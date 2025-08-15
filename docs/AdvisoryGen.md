# AdvisoryGen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** | not all of them have this | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gen import AdvisoryGen

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGen from a JSON string
advisory_gen_instance = AdvisoryGen.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGen.to_json())

# convert the object into a dict
advisory_gen_dict = advisory_gen_instance.to_dict()
# create an instance of AdvisoryGen from a dict
advisory_gen_from_dict = AdvisoryGen.from_dict(advisory_gen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


