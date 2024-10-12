# AdvisoryCVEReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cve_reference import AdvisoryCVEReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVEReference from a JSON string
advisory_cve_reference_instance = AdvisoryCVEReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVEReference.to_json())

# convert the object into a dict
advisory_cve_reference_dict = advisory_cve_reference_instance.to_dict()
# create an instance of AdvisoryCVEReference from a dict
advisory_cve_reference_from_dict = AdvisoryCVEReference.from_dict(advisory_cve_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


