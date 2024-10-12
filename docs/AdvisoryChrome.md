# AdvisoryChrome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_chrome import AdvisoryChrome

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryChrome from a JSON string
advisory_chrome_instance = AdvisoryChrome.from_json(json)
# print the JSON string representation of the object
print(AdvisoryChrome.to_json())

# convert the object into a dict
advisory_chrome_dict = advisory_chrome_instance.to_dict()
# create an instance of AdvisoryChrome from a dict
advisory_chrome_from_dict = AdvisoryChrome.from_dict(advisory_chrome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


