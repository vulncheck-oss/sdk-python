# AdvisoryMediatek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_chipsets** | **List[str]** |  | [optional] 
**affected_software** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mediatek import AdvisoryMediatek

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMediatek from a JSON string
advisory_mediatek_instance = AdvisoryMediatek.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMediatek.to_json())

# convert the object into a dict
advisory_mediatek_dict = advisory_mediatek_instance.to_dict()
# create an instance of AdvisoryMediatek from a dict
advisory_mediatek_from_dict = AdvisoryMediatek.from_dict(advisory_mediatek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


