# AdvisoryJNJAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_jnj_advisory import AdvisoryJNJAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJNJAdvisory from a JSON string
advisory_jnj_advisory_instance = AdvisoryJNJAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJNJAdvisory.to_json())

# convert the object into a dict
advisory_jnj_advisory_dict = advisory_jnj_advisory_instance.to_dict()
# create an instance of AdvisoryJNJAdvisory from a dict
advisory_jnj_advisory_from_dict = AdvisoryJNJAdvisory.from_dict(advisory_jnj_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


