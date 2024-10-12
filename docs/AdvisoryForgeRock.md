# AdvisoryForgeRock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_forge_rock import AdvisoryForgeRock

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryForgeRock from a JSON string
advisory_forge_rock_instance = AdvisoryForgeRock.from_json(json)
# print the JSON string representation of the object
print(AdvisoryForgeRock.to_json())

# convert the object into a dict
advisory_forge_rock_dict = advisory_forge_rock_instance.to_dict()
# create an instance of AdvisoryForgeRock from a dict
advisory_forge_rock_from_dict = AdvisoryForgeRock.from_dict(advisory_forge_rock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


