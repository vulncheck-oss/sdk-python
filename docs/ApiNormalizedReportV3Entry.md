# ApiNormalizedReportV3Entry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**refsource** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_normalized_report_v3_entry import ApiNormalizedReportV3Entry

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNormalizedReportV3Entry from a JSON string
api_normalized_report_v3_entry_instance = ApiNormalizedReportV3Entry.from_json(json)
# print the JSON string representation of the object
print(ApiNormalizedReportV3Entry.to_json())

# convert the object into a dict
api_normalized_report_v3_entry_dict = api_normalized_report_v3_entry_instance.to_dict()
# create an instance of ApiNormalizedReportV3Entry from a dict
api_normalized_report_v3_entry_from_dict = ApiNormalizedReportV3Entry.from_dict(api_normalized_report_v3_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


