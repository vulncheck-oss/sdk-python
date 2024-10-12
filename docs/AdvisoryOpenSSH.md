# AdvisoryOpenSSH


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_open_ssh import AdvisoryOpenSSH

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOpenSSH from a JSON string
advisory_open_ssh_instance = AdvisoryOpenSSH.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOpenSSH.to_json())

# convert the object into a dict
advisory_open_ssh_dict = advisory_open_ssh_instance.to_dict()
# create an instance of AdvisoryOpenSSH from a dict
advisory_open_ssh_from_dict = AdvisoryOpenSSH.from_dict(advisory_open_ssh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


