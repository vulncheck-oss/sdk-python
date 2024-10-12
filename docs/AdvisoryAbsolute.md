# AdvisoryAbsolute


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
from vulncheck_sdk.models.advisory_absolute import AdvisoryAbsolute

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAbsolute from a JSON string
advisory_absolute_instance = AdvisoryAbsolute.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAbsolute.to_json())

# convert the object into a dict
advisory_absolute_dict = advisory_absolute_instance.to_dict()
# create an instance of AdvisoryAbsolute from a dict
advisory_absolute_from_dict = AdvisoryAbsolute.from_dict(advisory_absolute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


