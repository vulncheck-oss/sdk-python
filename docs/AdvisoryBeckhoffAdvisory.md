# AdvisoryBeckhoffAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beckhoff_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_revised** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vde** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_beckhoff_advisory import AdvisoryBeckhoffAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBeckhoffAdvisory from a JSON string
advisory_beckhoff_advisory_instance = AdvisoryBeckhoffAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBeckhoffAdvisory.to_json())

# convert the object into a dict
advisory_beckhoff_advisory_dict = advisory_beckhoff_advisory_instance.to_dict()
# create an instance of AdvisoryBeckhoffAdvisory from a dict
advisory_beckhoff_advisory_from_dict = AdvisoryBeckhoffAdvisory.from_dict(advisory_beckhoff_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


