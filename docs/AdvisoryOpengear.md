# AdvisoryOpengear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_opengear import AdvisoryOpengear

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOpengear from a JSON string
advisory_opengear_instance = AdvisoryOpengear.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOpengear.to_json())

# convert the object into a dict
advisory_opengear_dict = advisory_opengear_instance.to_dict()
# create an instance of AdvisoryOpengear from a dict
advisory_opengear_from_dict = AdvisoryOpengear.from_dict(advisory_opengear_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


