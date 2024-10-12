# AdvisoryAppCheck


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
from vulncheck_sdk.models.advisory_app_check import AdvisoryAppCheck

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAppCheck from a JSON string
advisory_app_check_instance = AdvisoryAppCheck.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAppCheck.to_json())

# convert the object into a dict
advisory_app_check_dict = advisory_app_check_instance.to_dict()
# create an instance of AdvisoryAppCheck from a dict
advisory_app_check_from_dict = AdvisoryAppCheck.from_dict(advisory_app_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


