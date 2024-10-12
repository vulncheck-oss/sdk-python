# AdvisoryAMI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ami import AdvisoryAMI

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAMI from a JSON string
advisory_ami_instance = AdvisoryAMI.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAMI.to_json())

# convert the object into a dict
advisory_ami_dict = advisory_ami_instance.to_dict()
# create an instance of AdvisoryAMI from a dict
advisory_ami_from_dict = AdvisoryAMI.from_dict(advisory_ami_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


