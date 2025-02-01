# AdvisoryPyPAAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** | ID is the PYSEC- identifier | [optional] 
**affected** | [**List[AdvisoryPyPAAffected]**](AdvisoryPyPAAffected.md) | Affected will list out the vulnerable versions. | [optional] 
**aliases** | **List[str]** | Aliases are other identifiers that refer to this, such as a CVE | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** | Details discuss the vulnerability information | [optional] 
**modified** | **str** | Modified is non-zero Time if entry was updated | [optional] 
**published** | **str** | Published is the datetime when this was released | [optional] 
**references** | [**List[AdvisoryPyPAReference]**](AdvisoryPyPAReference.md) | References are links to more detailed advisories, fixes, etc. | [optional] 
**was_withdrawn** | **bool** | WasWD indicates if the advisory was withdrawn or not. | [optional] 
**withdrawn** | **str** | Withdrawn is non-zero if this advisory has been withdrawn | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_py_pa_advisory import AdvisoryPyPAAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPyPAAdvisory from a JSON string
advisory_py_pa_advisory_instance = AdvisoryPyPAAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPyPAAdvisory.to_json())

# convert the object into a dict
advisory_py_pa_advisory_dict = advisory_py_pa_advisory_instance.to_dict()
# create an instance of AdvisoryPyPAAdvisory from a dict
advisory_py_pa_advisory_from_dict = AdvisoryPyPAAdvisory.from_dict(advisory_py_pa_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


