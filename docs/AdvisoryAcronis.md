# AdvisoryAcronis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_acronis import AdvisoryAcronis

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAcronis from a JSON string
advisory_acronis_instance = AdvisoryAcronis.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAcronis.to_json())

# convert the object into a dict
advisory_acronis_dict = advisory_acronis_instance.to_dict()
# create an instance of AdvisoryAcronis from a dict
advisory_acronis_from_dict = AdvisoryAcronis.from_dict(advisory_acronis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


