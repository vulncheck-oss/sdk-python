# AdvisoryUSD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_usd import AdvisoryUSD

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryUSD from a JSON string
advisory_usd_instance = AdvisoryUSD.from_json(json)
# print the JSON string representation of the object
print(AdvisoryUSD.to_json())

# convert the object into a dict
advisory_usd_dict = advisory_usd_instance.to_dict()
# create an instance of AdvisoryUSD from a dict
advisory_usd_from_dict = AdvisoryUSD.from_dict(advisory_usd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


