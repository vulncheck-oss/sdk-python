# AdvisoryBDUSoft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**types** | [**AdvisoryBDUTypes**](AdvisoryBDUTypes.md) |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bdu_soft import AdvisoryBDUSoft

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUSoft from a JSON string
advisory_bdu_soft_instance = AdvisoryBDUSoft.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUSoft.to_json())

# convert the object into a dict
advisory_bdu_soft_dict = advisory_bdu_soft_instance.to_dict()
# create an instance of AdvisoryBDUSoft from a dict
advisory_bdu_soft_from_dict = AdvisoryBDUSoft.from_dict(advisory_bdu_soft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


