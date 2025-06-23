# AdvisoryCwe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cwe import AdvisoryCwe

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCwe from a JSON string
advisory_cwe_instance = AdvisoryCwe.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCwe.to_json())

# convert the object into a dict
advisory_cwe_dict = advisory_cwe_instance.to_dict()
# create an instance of AdvisoryCwe from a dict
advisory_cwe_from_dict = AdvisoryCwe.from_dict(advisory_cwe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


