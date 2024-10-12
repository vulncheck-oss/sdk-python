# AdvisoryMFiles


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
from vulncheck_sdk.models.advisory_m_files import AdvisoryMFiles

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMFiles from a JSON string
advisory_m_files_instance = AdvisoryMFiles.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMFiles.to_json())

# convert the object into a dict
advisory_m_files_dict = advisory_m_files_instance.to_dict()
# create an instance of AdvisoryMFiles from a dict
advisory_m_files_from_dict = AdvisoryMFiles.from_dict(advisory_m_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


