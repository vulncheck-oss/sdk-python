# AdvisoryCredit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_credit import AdvisoryCredit

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCredit from a JSON string
advisory_credit_instance = AdvisoryCredit.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCredit.to_json())

# convert the object into a dict
advisory_credit_dict = advisory_credit_instance.to_dict()
# create an instance of AdvisoryCredit from a dict
advisory_credit_from_dict = AdvisoryCredit.from_dict(advisory_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


