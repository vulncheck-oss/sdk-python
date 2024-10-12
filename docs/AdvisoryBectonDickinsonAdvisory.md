# AdvisoryBectonDickinsonAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**products_affected** | [**List[AdvisoryProductsAffected]**](AdvisoryProductsAffected.md) |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_becton_dickinson_advisory import AdvisoryBectonDickinsonAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBectonDickinsonAdvisory from a JSON string
advisory_becton_dickinson_advisory_instance = AdvisoryBectonDickinsonAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBectonDickinsonAdvisory.to_json())

# convert the object into a dict
advisory_becton_dickinson_advisory_dict = advisory_becton_dickinson_advisory_instance.to_dict()
# create an instance of AdvisoryBectonDickinsonAdvisory from a dict
advisory_becton_dickinson_advisory_from_dict = AdvisoryBectonDickinsonAdvisory.from_dict(advisory_becton_dickinson_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


