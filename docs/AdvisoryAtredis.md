# AdvisoryAtredis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendors** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_atredis import AdvisoryAtredis

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAtredis from a JSON string
advisory_atredis_instance = AdvisoryAtredis.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAtredis.to_json())

# convert the object into a dict
advisory_atredis_dict = advisory_atredis_instance.to_dict()
# create an instance of AdvisoryAtredis from a dict
advisory_atredis_from_dict = AdvisoryAtredis.from_dict(advisory_atredis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


