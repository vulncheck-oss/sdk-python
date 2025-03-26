# AdvisoryNetatalk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_netatalk import AdvisoryNetatalk

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNetatalk from a JSON string
advisory_netatalk_instance = AdvisoryNetatalk.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNetatalk.to_json())

# convert the object into a dict
advisory_netatalk_dict = advisory_netatalk_instance.to_dict()
# create an instance of AdvisoryNetatalk from a dict
advisory_netatalk_from_dict = AdvisoryNetatalk.from_dict(advisory_netatalk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


