# AdvisoryLinux


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
from vulncheck_sdk.models.advisory_linux import AdvisoryLinux

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryLinux from a JSON string
advisory_linux_instance = AdvisoryLinux.from_json(json)
# print the JSON string representation of the object
print(AdvisoryLinux.to_json())

# convert the object into a dict
advisory_linux_dict = advisory_linux_instance.to_dict()
# create an instance of AdvisoryLinux from a dict
advisory_linux_from_dict = AdvisoryLinux.from_dict(advisory_linux_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


