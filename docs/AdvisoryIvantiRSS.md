# AdvisoryIvantiRSS


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
from vulncheck_sdk.models.advisory_ivanti_rss import AdvisoryIvantiRSS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIvantiRSS from a JSON string
advisory_ivanti_rss_instance = AdvisoryIvantiRSS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIvantiRSS.to_json())

# convert the object into a dict
advisory_ivanti_rss_dict = advisory_ivanti_rss_instance.to_dict()
# create an instance of AdvisoryIvantiRSS from a dict
advisory_ivanti_rss_from_dict = AdvisoryIvantiRSS.from_dict(advisory_ivanti_rss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


