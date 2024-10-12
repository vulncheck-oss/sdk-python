# AdvisoryWibu


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_wibu import AdvisoryWibu

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWibu from a JSON string
advisory_wibu_instance = AdvisoryWibu.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWibu.to_json())

# convert the object into a dict
advisory_wibu_dict = advisory_wibu_instance.to_dict()
# create an instance of AdvisoryWibu from a dict
advisory_wibu_from_dict = AdvisoryWibu.from_dict(advisory_wibu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


