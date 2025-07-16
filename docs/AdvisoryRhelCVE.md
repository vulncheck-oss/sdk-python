# AdvisoryRhelCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf** | [**AdvisoryCSAF**](AdvisoryCSAF.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rhel_cve import AdvisoryRhelCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRhelCVE from a JSON string
advisory_rhel_cve_instance = AdvisoryRhelCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRhelCVE.to_json())

# convert the object into a dict
advisory_rhel_cve_dict = advisory_rhel_cve_instance.to_dict()
# create an instance of AdvisoryRhelCVE from a dict
advisory_rhel_cve_from_dict = AdvisoryRhelCVE.from_dict(advisory_rhel_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


