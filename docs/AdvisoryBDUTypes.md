# AdvisoryBDUTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bdu_types import AdvisoryBDUTypes

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUTypes from a JSON string
advisory_bdu_types_instance = AdvisoryBDUTypes.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUTypes.to_json())

# convert the object into a dict
advisory_bdu_types_dict = advisory_bdu_types_instance.to_dict()
# create an instance of AdvisoryBDUTypes from a dict
advisory_bdu_types_from_dict = AdvisoryBDUTypes.from_dict(advisory_bdu_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


