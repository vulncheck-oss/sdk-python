# AdvisoryCarrier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**affected_product** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_carrier import AdvisoryCarrier

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCarrier from a JSON string
advisory_carrier_instance = AdvisoryCarrier.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCarrier.to_json())

# convert the object into a dict
advisory_carrier_dict = advisory_carrier_instance.to_dict()
# create an instance of AdvisoryCarrier from a dict
advisory_carrier_from_dict = AdvisoryCarrier.from_dict(advisory_carrier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


