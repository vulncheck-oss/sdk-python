# AdvisoryAsus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_asus import AdvisoryAsus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAsus from a JSON string
advisory_asus_instance = AdvisoryAsus.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAsus.to_json())

# convert the object into a dict
advisory_asus_dict = advisory_asus_instance.to_dict()
# create an instance of AdvisoryAsus from a dict
advisory_asus_from_dict = AdvisoryAsus.from_dict(advisory_asus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


