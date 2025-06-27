# AdvisoryAffectedChrome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_version** | **str** |  | [optional] 
**product** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected_chrome import AdvisoryAffectedChrome

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffectedChrome from a JSON string
advisory_affected_chrome_instance = AdvisoryAffectedChrome.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffectedChrome.to_json())

# convert the object into a dict
advisory_affected_chrome_dict = advisory_affected_chrome_instance.to_dict()
# create an instance of AdvisoryAffectedChrome from a dict
advisory_affected_chrome_from_dict = AdvisoryAffectedChrome.from_dict(advisory_affected_chrome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


