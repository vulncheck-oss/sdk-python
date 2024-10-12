# AdvisoryNetgate


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
from vulncheck_sdk.models.advisory_netgate import AdvisoryNetgate

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNetgate from a JSON string
advisory_netgate_instance = AdvisoryNetgate.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNetgate.to_json())

# convert the object into a dict
advisory_netgate_dict = advisory_netgate_instance.to_dict()
# create an instance of AdvisoryNetgate from a dict
advisory_netgate_from_dict = AdvisoryNetgate.from_dict(advisory_netgate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


