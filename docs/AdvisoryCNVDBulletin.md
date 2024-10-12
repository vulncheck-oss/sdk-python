# AdvisoryCNVDBulletin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnta** | **str** |  | [optional] 
**cnvd** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**var_date** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**reference_urls** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cnvd_bulletin import AdvisoryCNVDBulletin

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCNVDBulletin from a JSON string
advisory_cnvd_bulletin_instance = AdvisoryCNVDBulletin.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCNVDBulletin.to_json())

# convert the object into a dict
advisory_cnvd_bulletin_dict = advisory_cnvd_bulletin_instance.to_dict()
# create an instance of AdvisoryCNVDBulletin from a dict
advisory_cnvd_bulletin_from_dict = AdvisoryCNVDBulletin.from_dict(advisory_cnvd_bulletin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


