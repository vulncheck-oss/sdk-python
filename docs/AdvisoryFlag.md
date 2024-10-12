# AdvisoryFlag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 
**label** | **str** |  | [optional] 
**product_ids** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_flag import AdvisoryFlag

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFlag from a JSON string
advisory_flag_instance = AdvisoryFlag.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFlag.to_json())

# convert the object into a dict
advisory_flag_dict = advisory_flag_instance.to_dict()
# create an instance of AdvisoryFlag from a dict
advisory_flag_from_dict = AdvisoryFlag.from_dict(advisory_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


