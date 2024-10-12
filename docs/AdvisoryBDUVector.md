# AdvisoryBDUVector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bdu_vector import AdvisoryBDUVector

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUVector from a JSON string
advisory_bdu_vector_instance = AdvisoryBDUVector.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUVector.to_json())

# convert the object into a dict
advisory_bdu_vector_dict = advisory_bdu_vector_instance.to_dict()
# create an instance of AdvisoryBDUVector from a dict
advisory_bdu_vector_from_dict = AdvisoryBDUVector.from_dict(advisory_bdu_vector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


