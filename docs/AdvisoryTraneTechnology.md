# AdvisoryTraneTechnology


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_trane_technology import AdvisoryTraneTechnology

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTraneTechnology from a JSON string
advisory_trane_technology_instance = AdvisoryTraneTechnology.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTraneTechnology.to_json())

# convert the object into a dict
advisory_trane_technology_dict = advisory_trane_technology_instance.to_dict()
# create an instance of AdvisoryTraneTechnology from a dict
advisory_trane_technology_from_dict = AdvisoryTraneTechnology.from_dict(advisory_trane_technology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


