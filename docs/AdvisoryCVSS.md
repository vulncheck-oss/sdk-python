# AdvisoryCVSS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**vector** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvss import AdvisoryCVSS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVSS from a JSON string
advisory_cvss_instance = AdvisoryCVSS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVSS.to_json())

# convert the object into a dict
advisory_cvss_dict = advisory_cvss_instance.to_dict()
# create an instance of AdvisoryCVSS from a dict
advisory_cvss_from_dict = AdvisoryCVSS.from_dict(advisory_cvss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


