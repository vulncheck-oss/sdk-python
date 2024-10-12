# AdvisoryJenkins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fix** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_jenkins import AdvisoryJenkins

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJenkins from a JSON string
advisory_jenkins_instance = AdvisoryJenkins.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJenkins.to_json())

# convert the object into a dict
advisory_jenkins_dict = advisory_jenkins_instance.to_dict()
# create an instance of AdvisoryJenkins from a dict
advisory_jenkins_from_dict = AdvisoryJenkins.from_dict(advisory_jenkins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


