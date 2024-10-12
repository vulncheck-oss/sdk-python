# AdvisoryLenovo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**industry_identifiers** | **List[str]** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**lenovo_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_lenovo import AdvisoryLenovo

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryLenovo from a JSON string
advisory_lenovo_instance = AdvisoryLenovo.from_json(json)
# print the JSON string representation of the object
print(AdvisoryLenovo.to_json())

# convert the object into a dict
advisory_lenovo_dict = advisory_lenovo_instance.to_dict()
# create an instance of AdvisoryLenovo from a dict
advisory_lenovo_from_dict = AdvisoryLenovo.from_dict(advisory_lenovo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


