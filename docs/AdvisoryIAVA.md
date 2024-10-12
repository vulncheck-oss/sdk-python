# AdvisoryIAVA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iava** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_iava import AdvisoryIAVA

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIAVA from a JSON string
advisory_iava_instance = AdvisoryIAVA.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIAVA.to_json())

# convert the object into a dict
advisory_iava_dict = advisory_iava_instance.to_dict()
# create an instance of AdvisoryIAVA from a dict
advisory_iava_from_dict = AdvisoryIAVA.from_dict(advisory_iava_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


