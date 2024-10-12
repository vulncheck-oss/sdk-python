# AdvisoryDraytek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_draytek import AdvisoryDraytek

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDraytek from a JSON string
advisory_draytek_instance = AdvisoryDraytek.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDraytek.to_json())

# convert the object into a dict
advisory_draytek_dict = advisory_draytek_instance.to_dict()
# create an instance of AdvisoryDraytek from a dict
advisory_draytek_from_dict = AdvisoryDraytek.from_dict(advisory_draytek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


