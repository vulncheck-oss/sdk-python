# AdvisorySecFix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**release** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sec_fix import AdvisorySecFix

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySecFix from a JSON string
advisory_sec_fix_instance = AdvisorySecFix.from_json(json)
# print the JSON string representation of the object
print(AdvisorySecFix.to_json())

# convert the object into a dict
advisory_sec_fix_dict = advisory_sec_fix_instance.to_dict()
# create an instance of AdvisorySecFix from a dict
advisory_sec_fix_from_dict = AdvisorySecFix.from_dict(advisory_sec_fix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


