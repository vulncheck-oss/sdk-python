# AdvisoryKoreLogic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_product** | **str** |  | [optional] 
**affected_vendor** | **str** |  | [optional] 
**affected_version** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_kore_logic import AdvisoryKoreLogic

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryKoreLogic from a JSON string
advisory_kore_logic_instance = AdvisoryKoreLogic.from_json(json)
# print the JSON string representation of the object
print(AdvisoryKoreLogic.to_json())

# convert the object into a dict
advisory_kore_logic_dict = advisory_kore_logic_instance.to_dict()
# create an instance of AdvisoryKoreLogic from a dict
advisory_kore_logic_from_dict = AdvisoryKoreLogic.from_dict(advisory_kore_logic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


