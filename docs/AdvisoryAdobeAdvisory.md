# AdvisoryAdobeAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryAdobeAffected]**](AdvisoryAdobeAffected.md) |  | [optional] 
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**solutions** | [**List[AdvisoryAdobeSolution]**](AdvisoryAdobeSolution.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_adobe_advisory import AdvisoryAdobeAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAdobeAdvisory from a JSON string
advisory_adobe_advisory_instance = AdvisoryAdobeAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAdobeAdvisory.to_json())

# convert the object into a dict
advisory_adobe_advisory_dict = advisory_adobe_advisory_instance.to_dict()
# create an instance of AdvisoryAdobeAdvisory from a dict
advisory_adobe_advisory_from_dict = AdvisoryAdobeAdvisory.from_dict(advisory_adobe_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


