# AdvisoryRustsecFrontMatterVersions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patched** | **List[str]** |  | [optional] 
**unaffected** | **List[str]** | Versions which were never vulnerable (optional) | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rustsec_front_matter_versions import AdvisoryRustsecFrontMatterVersions

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRustsecFrontMatterVersions from a JSON string
advisory_rustsec_front_matter_versions_instance = AdvisoryRustsecFrontMatterVersions.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRustsecFrontMatterVersions.to_json())

# convert the object into a dict
advisory_rustsec_front_matter_versions_dict = advisory_rustsec_front_matter_versions_instance.to_dict()
# create an instance of AdvisoryRustsecFrontMatterVersions from a dict
advisory_rustsec_front_matter_versions_from_dict = AdvisoryRustsecFrontMatterVersions.from_dict(advisory_rustsec_front_matter_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


