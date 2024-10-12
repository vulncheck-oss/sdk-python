# AdvisoryXylem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**xsa** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_xylem import AdvisoryXylem

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryXylem from a JSON string
advisory_xylem_instance = AdvisoryXylem.from_json(json)
# print the JSON string representation of the object
print(AdvisoryXylem.to_json())

# convert the object into a dict
advisory_xylem_dict = advisory_xylem_instance.to_dict()
# create an instance of AdvisoryXylem from a dict
advisory_xylem_from_dict = AdvisoryXylem.from_dict(advisory_xylem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


