# AdvisoryKRCertAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description_ko** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**overview_ko** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title_ko** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_kr_cert_advisory import AdvisoryKRCertAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryKRCertAdvisory from a JSON string
advisory_kr_cert_advisory_instance = AdvisoryKRCertAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryKRCertAdvisory.to_json())

# convert the object into a dict
advisory_kr_cert_advisory_dict = advisory_kr_cert_advisory_instance.to_dict()
# create an instance of AdvisoryKRCertAdvisory from a dict
advisory_kr_cert_advisory_from_dict = AdvisoryKRCertAdvisory.from_dict(advisory_kr_cert_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


