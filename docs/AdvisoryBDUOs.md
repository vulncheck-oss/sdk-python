# AdvisoryBDUOs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bduos import AdvisoryBDUOs

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUOs from a JSON string
advisory_bduos_instance = AdvisoryBDUOs.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUOs.to_json())

# convert the object into a dict
advisory_bduos_dict = advisory_bduos_instance.to_dict()
# create an instance of AdvisoryBDUOs from a dict
advisory_bduos_from_dict = AdvisoryBDUOs.from_dict(advisory_bduos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


