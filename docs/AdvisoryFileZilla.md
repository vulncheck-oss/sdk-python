# AdvisoryFileZilla


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
from vulncheck_sdk.models.advisory_file_zilla import AdvisoryFileZilla

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFileZilla from a JSON string
advisory_file_zilla_instance = AdvisoryFileZilla.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFileZilla.to_json())

# convert the object into a dict
advisory_file_zilla_dict = advisory_file_zilla_instance.to_dict()
# create an instance of AdvisoryFileZilla from a dict
advisory_file_zilla_from_dict = AdvisoryFileZilla.from_dict(advisory_file_zilla_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


