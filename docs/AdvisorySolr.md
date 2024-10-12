# AdvisorySolr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_solr import AdvisorySolr

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySolr from a JSON string
advisory_solr_instance = AdvisorySolr.from_json(json)
# print the JSON string representation of the object
print(AdvisorySolr.to_json())

# convert the object into a dict
advisory_solr_dict = advisory_solr_instance.to_dict()
# create an instance of AdvisorySolr from a dict
advisory_solr_from_dict = AdvisorySolr.from_dict(advisory_solr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


