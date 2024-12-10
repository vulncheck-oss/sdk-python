# AdvisoryMitreGroupCTI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | [**List[AdvisoryExternalReferences]**](AdvisoryExternalReferences.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mitre_group_cti import AdvisoryMitreGroupCTI

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMitreGroupCTI from a JSON string
advisory_mitre_group_cti_instance = AdvisoryMitreGroupCTI.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMitreGroupCTI.to_json())

# convert the object into a dict
advisory_mitre_group_cti_dict = advisory_mitre_group_cti_instance.to_dict()
# create an instance of AdvisoryMitreGroupCTI from a dict
advisory_mitre_group_cti_from_dict = AdvisoryMitreGroupCTI.from_dict(advisory_mitre_group_cti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


