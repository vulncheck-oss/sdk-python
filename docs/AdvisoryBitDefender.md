# AdvisoryBitDefender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_details** | **str** |  | [optional] 
**affected_products** | **str** |  | [optional] 
**affected_vendors** | **str** |  | [optional] 
**credit** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**timeline** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bit_defender import AdvisoryBitDefender

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBitDefender from a JSON string
advisory_bit_defender_instance = AdvisoryBitDefender.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBitDefender.to_json())

# convert the object into a dict
advisory_bit_defender_dict = advisory_bit_defender_instance.to_dict()
# create an instance of AdvisoryBitDefender from a dict
advisory_bit_defender_from_dict = AdvisoryBitDefender.from_dict(advisory_bit_defender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


