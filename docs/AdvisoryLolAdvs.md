# AdvisoryLolAdvs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**lol_json** | **Dict[str, object]** |  | [optional] 
**mitre_id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_lol_advs import AdvisoryLolAdvs

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryLolAdvs from a JSON string
advisory_lol_advs_instance = AdvisoryLolAdvs.from_json(json)
# print the JSON string representation of the object
print(AdvisoryLolAdvs.to_json())

# convert the object into a dict
advisory_lol_advs_dict = advisory_lol_advs_instance.to_dict()
# create an instance of AdvisoryLolAdvs from a dict
advisory_lol_advs_from_dict = AdvisoryLolAdvs.from_dict(advisory_lol_advs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


