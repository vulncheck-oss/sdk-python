# AdvisorySlackware


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
from vulncheck_sdk.models.advisory_slackware import AdvisorySlackware

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySlackware from a JSON string
advisory_slackware_instance = AdvisorySlackware.from_json(json)
# print the JSON string representation of the object
print(AdvisorySlackware.to_json())

# convert the object into a dict
advisory_slackware_dict = advisory_slackware_instance.to_dict()
# create an instance of AdvisorySlackware from a dict
advisory_slackware_from_dict = AdvisorySlackware.from_dict(advisory_slackware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


