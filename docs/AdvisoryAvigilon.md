# AdvisoryAvigilon


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
from vulncheck_sdk.models.advisory_avigilon import AdvisoryAvigilon

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAvigilon from a JSON string
advisory_avigilon_instance = AdvisoryAvigilon.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAvigilon.to_json())

# convert the object into a dict
advisory_avigilon_dict = advisory_avigilon_instance.to_dict()
# create an instance of AdvisoryAvigilon from a dict
advisory_avigilon_from_dict = AdvisoryAvigilon.from_dict(advisory_avigilon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


