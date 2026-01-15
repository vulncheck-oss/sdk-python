# AdvisoryMetaAdvisories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryMAffected]**](AdvisoryMAffected.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_meta_advisories import AdvisoryMetaAdvisories

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMetaAdvisories from a JSON string
advisory_meta_advisories_instance = AdvisoryMetaAdvisories.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMetaAdvisories.to_json())

# convert the object into a dict
advisory_meta_advisories_dict = advisory_meta_advisories_instance.to_dict()
# create an instance of AdvisoryMetaAdvisories from a dict
advisory_meta_advisories_from_dict = AdvisoryMetaAdvisories.from_dict(advisory_meta_advisories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


