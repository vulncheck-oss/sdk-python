# AdvisoryTalosAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**talos_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_talos_advisory import AdvisoryTalosAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTalosAdvisory from a JSON string
advisory_talos_advisory_instance = AdvisoryTalosAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTalosAdvisory.to_json())

# convert the object into a dict
advisory_talos_advisory_dict = advisory_talos_advisory_instance.to_dict()
# create an instance of AdvisoryTalosAdvisory from a dict
advisory_talos_advisory_from_dict = AdvisoryTalosAdvisory.from_dict(advisory_talos_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


