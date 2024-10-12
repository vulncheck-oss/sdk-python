# AdvisoryMReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_reference import AdvisoryMReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMReference from a JSON string
advisory_m_reference_instance = AdvisoryMReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMReference.to_json())

# convert the object into a dict
advisory_m_reference_dict = advisory_m_reference_instance.to_dict()
# create an instance of AdvisoryMReference from a dict
advisory_m_reference_from_dict = AdvisoryMReference.from_dict(advisory_m_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


