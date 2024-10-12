# AdvisoryZeroDayAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**zdi** | [**AdvisoryZDI**](AdvisoryZDI.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zero_day_advisory import AdvisoryZeroDayAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZeroDayAdvisory from a JSON string
advisory_zero_day_advisory_instance = AdvisoryZeroDayAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZeroDayAdvisory.to_json())

# convert the object into a dict
advisory_zero_day_advisory_dict = advisory_zero_day_advisory_instance.to_dict()
# create an instance of AdvisoryZeroDayAdvisory from a dict
advisory_zero_day_advisory_from_dict = AdvisoryZeroDayAdvisory.from_dict(advisory_zero_day_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


