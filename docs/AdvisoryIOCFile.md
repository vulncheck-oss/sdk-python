# AdvisoryIOCFile

advisory.IOCFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ioc_file import AdvisoryIOCFile

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIOCFile from a JSON string
advisory_ioc_file_instance = AdvisoryIOCFile.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIOCFile.to_json())

# convert the object into a dict
advisory_ioc_file_dict = advisory_ioc_file_instance.to_dict()
# create an instance of AdvisoryIOCFile from a dict
advisory_ioc_file_from_dict = AdvisoryIOCFile.from_dict(advisory_ioc_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


