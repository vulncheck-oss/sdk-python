# AdvisoryBaxterAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_updated** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_baxter_advisory import AdvisoryBaxterAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBaxterAdvisory from a JSON string
advisory_baxter_advisory_instance = AdvisoryBaxterAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBaxterAdvisory.to_json())

# convert the object into a dict
advisory_baxter_advisory_dict = advisory_baxter_advisory_instance.to_dict()
# create an instance of AdvisoryBaxterAdvisory from a dict
advisory_baxter_advisory_from_dict = AdvisoryBaxterAdvisory.from_dict(advisory_baxter_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


