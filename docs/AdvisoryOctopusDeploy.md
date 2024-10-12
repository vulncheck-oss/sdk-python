# AdvisoryOctopusDeploy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_number** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_octopus_deploy import AdvisoryOctopusDeploy

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOctopusDeploy from a JSON string
advisory_octopus_deploy_instance = AdvisoryOctopusDeploy.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOctopusDeploy.to_json())

# convert the object into a dict
advisory_octopus_deploy_dict = advisory_octopus_deploy_instance.to_dict()
# create an instance of AdvisoryOctopusDeploy from a dict
advisory_octopus_deploy_from_dict = AdvisoryOctopusDeploy.from_dict(advisory_octopus_deploy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


