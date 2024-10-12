# AdvisoryMitreCVEListV5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**mitre_ref** | [**AdvisoryMitreCVEListV5Ref**](AdvisoryMitreCVEListV5Ref.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mitre_cve_list_v5 import AdvisoryMitreCVEListV5

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMitreCVEListV5 from a JSON string
advisory_mitre_cve_list_v5_instance = AdvisoryMitreCVEListV5.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMitreCVEListV5.to_json())

# convert the object into a dict
advisory_mitre_cve_list_v5_dict = advisory_mitre_cve_list_v5_instance.to_dict()
# create an instance of AdvisoryMitreCVEListV5 from a dict
advisory_mitre_cve_list_v5_from_dict = AdvisoryMitreCVEListV5.from_dict(advisory_mitre_cve_list_v5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


