# AdvisoryElastic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**esaid** | **str** |  | [optional] 
**remediation** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_elastic import AdvisoryElastic

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryElastic from a JSON string
advisory_elastic_instance = AdvisoryElastic.from_json(json)
# print the JSON string representation of the object
print(AdvisoryElastic.to_json())

# convert the object into a dict
advisory_elastic_dict = advisory_elastic_instance.to_dict()
# create an instance of AdvisoryElastic from a dict
advisory_elastic_from_dict = AdvisoryElastic.from_dict(advisory_elastic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


