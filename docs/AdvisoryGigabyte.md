# AdvisoryGigabyte


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gigabyte import AdvisoryGigabyte

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGigabyte from a JSON string
advisory_gigabyte_instance = AdvisoryGigabyte.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGigabyte.to_json())

# convert the object into a dict
advisory_gigabyte_dict = advisory_gigabyte_instance.to_dict()
# create an instance of AdvisoryGigabyte from a dict
advisory_gigabyte_from_dict = AdvisoryGigabyte.from_dict(advisory_gigabyte_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


