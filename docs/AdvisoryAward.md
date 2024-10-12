# AdvisoryAward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_award import AdvisoryAward

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAward from a JSON string
advisory_award_instance = AdvisoryAward.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAward.to_json())

# convert the object into a dict
advisory_award_dict = advisory_award_instance.to_dict()
# create an instance of AdvisoryAward from a dict
advisory_award_from_dict = AdvisoryAward.from_dict(advisory_award_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


