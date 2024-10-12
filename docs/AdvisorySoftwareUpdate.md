# AdvisorySoftwareUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_version** | **str** |  | [optional] 
**cves** | **List[str]** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**software_product** | **str** |  | [optional] 
**updated_version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_software_update import AdvisorySoftwareUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySoftwareUpdate from a JSON string
advisory_software_update_instance = AdvisorySoftwareUpdate.from_json(json)
# print the JSON string representation of the object
print(AdvisorySoftwareUpdate.to_json())

# convert the object into a dict
advisory_software_update_dict = advisory_software_update_instance.to_dict()
# create an instance of AdvisorySoftwareUpdate from a dict
advisory_software_update_from_dict = AdvisorySoftwareUpdate.from_dict(advisory_software_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


