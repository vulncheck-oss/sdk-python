# AdvisoryXDB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_ssh_url** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**exploit_type** | **str** |  | [optional] 
**xdb_id** | **str** |  | [optional] 
**xdb_url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_xdb import AdvisoryXDB

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryXDB from a JSON string
advisory_xdb_instance = AdvisoryXDB.from_json(json)
# print the JSON string representation of the object
print(AdvisoryXDB.to_json())

# convert the object into a dict
advisory_xdb_dict = advisory_xdb_instance.to_dict()
# create an instance of AdvisoryXDB from a dict
advisory_xdb_from_dict = AdvisoryXDB.from_dict(advisory_xdb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


