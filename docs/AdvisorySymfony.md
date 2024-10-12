# AdvisorySymfony


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_symfony import AdvisorySymfony

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySymfony from a JSON string
advisory_symfony_instance = AdvisorySymfony.from_json(json)
# print the JSON string representation of the object
print(AdvisorySymfony.to_json())

# convert the object into a dict
advisory_symfony_dict = advisory_symfony_instance.to_dict()
# create an instance of AdvisorySymfony from a dict
advisory_symfony_from_dict = AdvisorySymfony.from_dict(advisory_symfony_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


