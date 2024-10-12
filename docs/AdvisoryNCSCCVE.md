# AdvisoryNCSCCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf** | [**AdvisoryCSAF**](AdvisoryCSAF.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary_nl** | **str** |  | [optional] 
**title_nl** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ncsccve import AdvisoryNCSCCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNCSCCVE from a JSON string
advisory_ncsccve_instance = AdvisoryNCSCCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNCSCCVE.to_json())

# convert the object into a dict
advisory_ncsccve_dict = advisory_ncsccve_instance.to_dict()
# create an instance of AdvisoryNCSCCVE from a dict
advisory_ncsccve_from_dict = AdvisoryNCSCCVE.from_dict(advisory_ncsccve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


