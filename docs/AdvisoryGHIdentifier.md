# AdvisoryGHIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gh_identifier import AdvisoryGHIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHIdentifier from a JSON string
advisory_gh_identifier_instance = AdvisoryGHIdentifier.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHIdentifier.to_json())

# convert the object into a dict
advisory_gh_identifier_dict = advisory_gh_identifier_instance.to_dict()
# create an instance of AdvisoryGHIdentifier from a dict
advisory_gh_identifier_from_dict = AdvisoryGHIdentifier.from_dict(advisory_gh_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


