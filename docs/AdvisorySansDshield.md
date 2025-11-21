# AdvisorySansDshield


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**first_seen** | **str** |  | [optional] 
**last_seen** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sans_dshield import AdvisorySansDshield

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySansDshield from a JSON string
advisory_sans_dshield_instance = AdvisorySansDshield.from_json(json)
# print the JSON string representation of the object
print(AdvisorySansDshield.to_json())

# convert the object into a dict
advisory_sans_dshield_dict = advisory_sans_dshield_instance.to_dict()
# create an instance of AdvisorySansDshield from a dict
advisory_sans_dshield_from_dict = AdvisorySansDshield.from_dict(advisory_sans_dshield_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


