# AdvisoryNetskope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_netskope import AdvisoryNetskope

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNetskope from a JSON string
advisory_netskope_instance = AdvisoryNetskope.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNetskope.to_json())

# convert the object into a dict
advisory_netskope_dict = advisory_netskope_instance.to_dict()
# create an instance of AdvisoryNetskope from a dict
advisory_netskope_from_dict = AdvisoryNetskope.from_dict(advisory_netskope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


