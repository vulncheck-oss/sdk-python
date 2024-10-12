# AdvisoryDebianCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**debianbug** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**releases** | [**List[AdvisoryAffectedDebianRelease]**](AdvisoryAffectedDebianRelease.md) |  | [optional] 
**scope** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_debian_cve import AdvisoryDebianCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDebianCVE from a JSON string
advisory_debian_cve_instance = AdvisoryDebianCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDebianCVE.to_json())

# convert the object into a dict
advisory_debian_cve_dict = advisory_debian_cve_instance.to_dict()
# create an instance of AdvisoryDebianCVE from a dict
advisory_debian_cve_from_dict = AdvisoryDebianCVE.from_dict(advisory_debian_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


