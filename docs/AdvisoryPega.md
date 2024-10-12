# AdvisoryPega


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**score** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_pega import AdvisoryPega

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPega from a JSON string
advisory_pega_instance = AdvisoryPega.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPega.to_json())

# convert the object into a dict
advisory_pega_dict = advisory_pega_instance.to_dict()
# create an instance of AdvisoryPega from a dict
advisory_pega_from_dict = AdvisoryPega.from_dict(advisory_pega_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


