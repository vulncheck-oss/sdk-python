# AdvisorySyss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_syss import AdvisorySyss

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySyss from a JSON string
advisory_syss_instance = AdvisorySyss.from_json(json)
# print the JSON string representation of the object
print(AdvisorySyss.to_json())

# convert the object into a dict
advisory_syss_dict = advisory_syss_instance.to_dict()
# create an instance of AdvisorySyss from a dict
advisory_syss_from_dict = AdvisorySyss.from_dict(advisory_syss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


