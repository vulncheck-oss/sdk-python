# AdvisoryLantronix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_lantronix import AdvisoryLantronix

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryLantronix from a JSON string
advisory_lantronix_instance = AdvisoryLantronix.from_json(json)
# print the JSON string representation of the object
print(AdvisoryLantronix.to_json())

# convert the object into a dict
advisory_lantronix_dict = advisory_lantronix_instance.to_dict()
# create an instance of AdvisoryLantronix from a dict
advisory_lantronix_from_dict = AdvisoryLantronix.from_dict(advisory_lantronix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


