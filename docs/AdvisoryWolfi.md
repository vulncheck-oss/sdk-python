# AdvisoryWolfi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apkurl** | **str** |  | [optional] 
**archs** | **List[str]** |  | [optional] 
**date_added** | **str** | un-used | [optional] 
**packages** | [**List[AdvisoryWolfiPackage]**](AdvisoryWolfiPackage.md) |  | [optional] 
**reponame** | **str** |  | [optional] 
**urlprefix** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_wolfi import AdvisoryWolfi

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWolfi from a JSON string
advisory_wolfi_instance = AdvisoryWolfi.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWolfi.to_json())

# convert the object into a dict
advisory_wolfi_dict = advisory_wolfi_instance.to_dict()
# create an instance of AdvisoryWolfi from a dict
advisory_wolfi_from_dict = AdvisoryWolfi.from_dict(advisory_wolfi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


