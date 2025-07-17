# AdvisoryHacktivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**float64** | **float** |  | [optional] 
**rank** | **int** |  | [optional] 
**reports_submitted** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hacktivity import AdvisoryHacktivity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHacktivity from a JSON string
advisory_hacktivity_instance = AdvisoryHacktivity.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHacktivity.to_json())

# convert the object into a dict
advisory_hacktivity_dict = advisory_hacktivity_instance.to_dict()
# create an instance of AdvisoryHacktivity from a dict
advisory_hacktivity_from_dict = AdvisoryHacktivity.from_dict(advisory_hacktivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


