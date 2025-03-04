# AdvisoryOpenJDKCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_open_jdkcve import AdvisoryOpenJDKCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOpenJDKCVE from a JSON string
advisory_open_jdkcve_instance = AdvisoryOpenJDKCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOpenJDKCVE.to_json())

# convert the object into a dict
advisory_open_jdkcve_dict = advisory_open_jdkcve_instance.to_dict()
# create an instance of AdvisoryOpenJDKCVE from a dict
advisory_open_jdkcve_from_dict = AdvisoryOpenJDKCVE.from_dict(advisory_open_jdkcve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


