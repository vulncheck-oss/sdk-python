# AdvisoryCarestreamAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carestream_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_updated** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_carestream_advisory import AdvisoryCarestreamAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCarestreamAdvisory from a JSON string
advisory_carestream_advisory_instance = AdvisoryCarestreamAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCarestreamAdvisory.to_json())

# convert the object into a dict
advisory_carestream_advisory_dict = advisory_carestream_advisory_instance.to_dict()
# create an instance of AdvisoryCarestreamAdvisory from a dict
advisory_carestream_advisory_from_dict = AdvisoryCarestreamAdvisory.from_dict(advisory_carestream_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


