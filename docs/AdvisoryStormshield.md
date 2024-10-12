# AdvisoryStormshield


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_stormshield import AdvisoryStormshield

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryStormshield from a JSON string
advisory_stormshield_instance = AdvisoryStormshield.from_json(json)
# print the JSON string representation of the object
print(AdvisoryStormshield.to_json())

# convert the object into a dict
advisory_stormshield_dict = advisory_stormshield_instance.to_dict()
# create an instance of AdvisoryStormshield from a dict
advisory_stormshield_from_dict = AdvisoryStormshield.from_dict(advisory_stormshield_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


