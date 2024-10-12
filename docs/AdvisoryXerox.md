# AdvisoryXerox


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
from vulncheck_sdk.models.advisory_xerox import AdvisoryXerox

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryXerox from a JSON string
advisory_xerox_instance = AdvisoryXerox.from_json(json)
# print the JSON string representation of the object
print(AdvisoryXerox.to_json())

# convert the object into a dict
advisory_xerox_dict = advisory_xerox_instance.to_dict()
# create an instance of AdvisoryXerox from a dict
advisory_xerox_from_dict = AdvisoryXerox.from_dict(advisory_xerox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


