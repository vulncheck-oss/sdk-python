# AdvisoryCVRFReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvrf_reference import AdvisoryCVRFReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVRFReference from a JSON string
advisory_cvrf_reference_instance = AdvisoryCVRFReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVRFReference.to_json())

# convert the object into a dict
advisory_cvrf_reference_dict = advisory_cvrf_reference_instance.to_dict()
# create an instance of AdvisoryCVRFReference from a dict
advisory_cvrf_reference_from_dict = AdvisoryCVRFReference.from_dict(advisory_cvrf_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


