# AdvisoryGHCvss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** |  | [optional] 
**vector_string** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gh_cvss import AdvisoryGHCvss

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHCvss from a JSON string
advisory_gh_cvss_instance = AdvisoryGHCvss.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHCvss.to_json())

# convert the object into a dict
advisory_gh_cvss_dict = advisory_gh_cvss_instance.to_dict()
# create an instance of AdvisoryGHCvss from a dict
advisory_gh_cvss_from_dict = AdvisoryGHCvss.from_dict(advisory_gh_cvss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


