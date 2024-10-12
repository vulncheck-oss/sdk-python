# AdvisoryDjango


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_django import AdvisoryDjango

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDjango from a JSON string
advisory_django_instance = AdvisoryDjango.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDjango.to_json())

# convert the object into a dict
advisory_django_dict = advisory_django_instance.to_dict()
# create an instance of AdvisoryDjango from a dict
advisory_django_from_dict = AdvisoryDjango.from_dict(advisory_django_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


