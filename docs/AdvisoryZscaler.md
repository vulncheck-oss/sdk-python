# AdvisoryZscaler


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zscaler import AdvisoryZscaler

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZscaler from a JSON string
advisory_zscaler_instance = AdvisoryZscaler.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZscaler.to_json())

# convert the object into a dict
advisory_zscaler_dict = advisory_zscaler_instance.to_dict()
# create an instance of AdvisoryZscaler from a dict
advisory_zscaler_from_dict = AdvisoryZscaler.from_dict(advisory_zscaler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


