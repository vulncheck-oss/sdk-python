# AdvisoryFoxit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryFoxitAffected]**](AdvisoryFoxitAffected.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_foxit import AdvisoryFoxit

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFoxit from a JSON string
advisory_foxit_instance = AdvisoryFoxit.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFoxit.to_json())

# convert the object into a dict
advisory_foxit_dict = advisory_foxit_instance.to_dict()
# create an instance of AdvisoryFoxit from a dict
advisory_foxit_from_dict = AdvisoryFoxit.from_dict(advisory_foxit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


