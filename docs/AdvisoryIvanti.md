# AdvisoryIvanti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ivanti import AdvisoryIvanti

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIvanti from a JSON string
advisory_ivanti_instance = AdvisoryIvanti.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIvanti.to_json())

# convert the object into a dict
advisory_ivanti_dict = advisory_ivanti_instance.to_dict()
# create an instance of AdvisoryIvanti from a dict
advisory_ivanti_from_dict = AdvisoryIvanti.from_dict(advisory_ivanti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


