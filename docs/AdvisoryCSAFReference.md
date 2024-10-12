# AdvisoryCSAFReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_csaf_reference import AdvisoryCSAFReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCSAFReference from a JSON string
advisory_csaf_reference_instance = AdvisoryCSAFReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCSAFReference.to_json())

# convert the object into a dict
advisory_csaf_reference_dict = advisory_csaf_reference_instance.to_dict()
# create an instance of AdvisoryCSAFReference from a dict
advisory_csaf_reference_from_dict = AdvisoryCSAFReference.from_dict(advisory_csaf_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


