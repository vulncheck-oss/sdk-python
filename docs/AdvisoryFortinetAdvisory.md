# AdvisoryFortinetAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgement** | **str** |  | [optional] 
**affected_products** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvssv3** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**irnumber** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**solutions** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_fortinet_advisory import AdvisoryFortinetAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFortinetAdvisory from a JSON string
advisory_fortinet_advisory_instance = AdvisoryFortinetAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFortinetAdvisory.to_json())

# convert the object into a dict
advisory_fortinet_advisory_dict = advisory_fortinet_advisory_instance.to_dict()
# create an instance of AdvisoryFortinetAdvisory from a dict
advisory_fortinet_advisory_from_dict = AdvisoryFortinetAdvisory.from_dict(advisory_fortinet_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


