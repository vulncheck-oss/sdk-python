# AdvisoryVanDyke


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_van_dyke import AdvisoryVanDyke

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVanDyke from a JSON string
advisory_van_dyke_instance = AdvisoryVanDyke.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVanDyke.to_json())

# convert the object into a dict
advisory_van_dyke_dict = advisory_van_dyke_instance.to_dict()
# create an instance of AdvisoryVanDyke from a dict
advisory_van_dyke_from_dict = AdvisoryVanDyke.from_dict(advisory_van_dyke_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


