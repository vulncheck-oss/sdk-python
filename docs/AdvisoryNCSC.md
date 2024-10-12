# AdvisoryNCSC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf** | [**AdvisoryCSAF**](AdvisoryCSAF.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary_nl** | **str** |  | [optional] 
**title_nl** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ncsc import AdvisoryNCSC

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNCSC from a JSON string
advisory_ncsc_instance = AdvisoryNCSC.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNCSC.to_json())

# convert the object into a dict
advisory_ncsc_dict = advisory_ncsc_instance.to_dict()
# create an instance of AdvisoryNCSC from a dict
advisory_ncsc_from_dict = AdvisoryNCSC.from_dict(advisory_ncsc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


