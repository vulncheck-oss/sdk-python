# AdvisoryDanFossCVEDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **str** |  | [optional] 
**cve** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_dan_foss_cve_details import AdvisoryDanFossCVEDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDanFossCVEDetails from a JSON string
advisory_dan_foss_cve_details_instance = AdvisoryDanFossCVEDetails.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDanFossCVEDetails.to_json())

# convert the object into a dict
advisory_dan_foss_cve_details_dict = advisory_dan_foss_cve_details_instance.to_dict()
# create an instance of AdvisoryDanFossCVEDetails from a dict
advisory_dan_foss_cve_details_from_dict = AdvisoryDanFossCVEDetails.from_dict(advisory_dan_foss_cve_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


