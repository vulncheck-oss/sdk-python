# AdvisoryOpenJDK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**openjdk_cves** | [**List[AdvisoryOpenJDKCVE]**](AdvisoryOpenJDKCVE.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_open_jdk import AdvisoryOpenJDK

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOpenJDK from a JSON string
advisory_open_jdk_instance = AdvisoryOpenJDK.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOpenJDK.to_json())

# convert the object into a dict
advisory_open_jdk_dict = advisory_open_jdk_instance.to_dict()
# create an instance of AdvisoryOpenJDK from a dict
advisory_open_jdk_from_dict = AdvisoryOpenJDK.from_dict(advisory_open_jdk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


