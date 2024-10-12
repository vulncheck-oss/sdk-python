# AdvisoryPalantir


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**background** | **str** |  | [optional] 
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_palantir import AdvisoryPalantir

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPalantir from a JSON string
advisory_palantir_instance = AdvisoryPalantir.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPalantir.to_json())

# convert the object into a dict
advisory_palantir_dict = advisory_palantir_instance.to_dict()
# create an instance of AdvisoryPalantir from a dict
advisory_palantir_from_dict = AdvisoryPalantir.from_dict(advisory_palantir_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


