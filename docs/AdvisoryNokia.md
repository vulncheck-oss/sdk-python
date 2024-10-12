# AdvisoryNokia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nokia import AdvisoryNokia

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNokia from a JSON string
advisory_nokia_instance = AdvisoryNokia.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNokia.to_json())

# convert the object into a dict
advisory_nokia_dict = advisory_nokia_instance.to_dict()
# create an instance of AdvisoryNokia from a dict
advisory_nokia_from_dict = AdvisoryNokia.from_dict(advisory_nokia_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


