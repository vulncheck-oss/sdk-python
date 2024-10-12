# AdvisoryBlackBerry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bsrt** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_black_berry import AdvisoryBlackBerry

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBlackBerry from a JSON string
advisory_black_berry_instance = AdvisoryBlackBerry.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBlackBerry.to_json())

# convert the object into a dict
advisory_black_berry_dict = advisory_black_berry_instance.to_dict()
# create an instance of AdvisoryBlackBerry from a dict
advisory_black_berry_from_dict = AdvisoryBlackBerry.from_dict(advisory_black_berry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


