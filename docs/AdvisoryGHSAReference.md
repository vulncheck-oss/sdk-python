# AdvisoryGHSAReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ghsa_reference import AdvisoryGHSAReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHSAReference from a JSON string
advisory_ghsa_reference_instance = AdvisoryGHSAReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHSAReference.to_json())

# convert the object into a dict
advisory_ghsa_reference_dict = advisory_ghsa_reference_instance.to_dict()
# create an instance of AdvisoryGHSAReference from a dict
advisory_ghsa_reference_from_dict = AdvisoryGHSAReference.from_dict(advisory_ghsa_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


