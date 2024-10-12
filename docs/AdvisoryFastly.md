# AdvisoryFastly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_fastly import AdvisoryFastly

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFastly from a JSON string
advisory_fastly_instance = AdvisoryFastly.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFastly.to_json())

# convert the object into a dict
advisory_fastly_dict = advisory_fastly_instance.to_dict()
# create an instance of AdvisoryFastly from a dict
advisory_fastly_from_dict = AdvisoryFastly.from_dict(advisory_fastly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


