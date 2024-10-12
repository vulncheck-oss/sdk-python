# AdvisoryMitreCVEListV5Ref


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**AdvisoryMContainers**](AdvisoryMContainers.md) |  | [optional] 
**cve_metadata** | [**AdvisoryMCveMetadata**](AdvisoryMCveMetadata.md) |  | [optional] 
**data_type** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mitre_cve_list_v5_ref import AdvisoryMitreCVEListV5Ref

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMitreCVEListV5Ref from a JSON string
advisory_mitre_cve_list_v5_ref_instance = AdvisoryMitreCVEListV5Ref.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMitreCVEListV5Ref.to_json())

# convert the object into a dict
advisory_mitre_cve_list_v5_ref_dict = advisory_mitre_cve_list_v5_ref_instance.to_dict()
# create an instance of AdvisoryMitreCVEListV5Ref from a dict
advisory_mitre_cve_list_v5_ref_from_dict = AdvisoryMitreCVEListV5Ref.from_dict(advisory_mitre_cve_list_v5_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


