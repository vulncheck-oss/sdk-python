# AdvisoryCBLMariner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**package** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cbl_mariner import AdvisoryCBLMariner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCBLMariner from a JSON string
advisory_cbl_mariner_instance = AdvisoryCBLMariner.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCBLMariner.to_json())

# convert the object into a dict
advisory_cbl_mariner_dict = advisory_cbl_mariner_instance.to_dict()
# create an instance of AdvisoryCBLMariner from a dict
advisory_cbl_mariner_from_dict = AdvisoryCBLMariner.from_dict(advisory_cbl_mariner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


