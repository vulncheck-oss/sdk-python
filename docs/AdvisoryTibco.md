# AdvisoryTibco


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tibco import AdvisoryTibco

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTibco from a JSON string
advisory_tibco_instance = AdvisoryTibco.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTibco.to_json())

# convert the object into a dict
advisory_tibco_dict = advisory_tibco_instance.to_dict()
# create an instance of AdvisoryTibco from a dict
advisory_tibco_from_dict = AdvisoryTibco.from_dict(advisory_tibco_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


