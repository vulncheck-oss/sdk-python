# AdvisoryRThreat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**date_specified** | **bool** |  | [optional] 
**description** | [**AdvisoryIVal**](AdvisoryIVal.md) |  | [optional] 
**product_id** | **List[str]** |  | [optional] 
**type** | **int** | diff | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_r_threat import AdvisoryRThreat

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRThreat from a JSON string
advisory_r_threat_instance = AdvisoryRThreat.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRThreat.to_json())

# convert the object into a dict
advisory_r_threat_dict = advisory_r_threat_instance.to_dict()
# create an instance of AdvisoryRThreat from a dict
advisory_r_threat_from_dict = AdvisoryRThreat.from_dict(advisory_r_threat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


