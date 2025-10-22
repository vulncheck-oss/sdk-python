# AdvisoryGHSARange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AdvisoryGHSAEvent]**](AdvisoryGHSAEvent.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ghsa_range import AdvisoryGHSARange

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHSARange from a JSON string
advisory_ghsa_range_instance = AdvisoryGHSARange.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHSARange.to_json())

# convert the object into a dict
advisory_ghsa_range_dict = advisory_ghsa_range_instance.to_dict()
# create an instance of AdvisoryGHSARange from a dict
advisory_ghsa_range_from_dict = AdvisoryGHSARange.from_dict(advisory_ghsa_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


