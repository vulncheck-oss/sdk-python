# AdvisoryMoxaAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_moxa_advisory import AdvisoryMoxaAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMoxaAdvisory from a JSON string
advisory_moxa_advisory_instance = AdvisoryMoxaAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMoxaAdvisory.to_json())

# convert the object into a dict
advisory_moxa_advisory_dict = advisory_moxa_advisory_instance.to_dict()
# create an instance of AdvisoryMoxaAdvisory from a dict
advisory_moxa_advisory_from_dict = AdvisoryMoxaAdvisory.from_dict(advisory_moxa_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


