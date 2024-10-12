# AdvisoryQualys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**exploits** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_qualys import AdvisoryQualys

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryQualys from a JSON string
advisory_qualys_instance = AdvisoryQualys.from_json(json)
# print the JSON string representation of the object
print(AdvisoryQualys.to_json())

# convert the object into a dict
advisory_qualys_dict = advisory_qualys_instance.to_dict()
# create an instance of AdvisoryQualys from a dict
advisory_qualys_from_dict = AdvisoryQualys.from_dict(advisory_qualys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


