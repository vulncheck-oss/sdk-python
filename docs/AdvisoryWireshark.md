# AdvisoryWireshark


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_wireshark import AdvisoryWireshark

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWireshark from a JSON string
advisory_wireshark_instance = AdvisoryWireshark.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWireshark.to_json())

# convert the object into a dict
advisory_wireshark_dict = advisory_wireshark_instance.to_dict()
# create an instance of AdvisoryWireshark from a dict
advisory_wireshark_from_dict = AdvisoryWireshark.from_dict(advisory_wireshark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


