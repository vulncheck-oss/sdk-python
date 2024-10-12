# AdvisoryGCP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gcp import AdvisoryGCP

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGCP from a JSON string
advisory_gcp_instance = AdvisoryGCP.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGCP.to_json())

# convert the object into a dict
advisory_gcp_dict = advisory_gcp_instance.to_dict()
# create an instance of AdvisoryGCP from a dict
advisory_gcp_from_dict = AdvisoryGCP.from_dict(advisory_gcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


