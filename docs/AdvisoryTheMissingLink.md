# AdvisoryTheMissingLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_versions** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed_versions** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_the_missing_link import AdvisoryTheMissingLink

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTheMissingLink from a JSON string
advisory_the_missing_link_instance = AdvisoryTheMissingLink.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTheMissingLink.to_json())

# convert the object into a dict
advisory_the_missing_link_dict = advisory_the_missing_link_instance.to_dict()
# create an instance of AdvisoryTheMissingLink from a dict
advisory_the_missing_link_from_dict = AdvisoryTheMissingLink.from_dict(advisory_the_missing_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


