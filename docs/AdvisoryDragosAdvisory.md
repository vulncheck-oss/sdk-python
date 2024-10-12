# AdvisoryDragosAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_dragos_advisory import AdvisoryDragosAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDragosAdvisory from a JSON string
advisory_dragos_advisory_instance = AdvisoryDragosAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDragosAdvisory.to_json())

# convert the object into a dict
advisory_dragos_advisory_dict = advisory_dragos_advisory_instance.to_dict()
# create an instance of AdvisoryDragosAdvisory from a dict
advisory_dragos_advisory_from_dict = AdvisoryDragosAdvisory.from_dict(advisory_dragos_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


