# AdvisoryCirclContainers

advisory.CirclContainers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adp** | [**List[AdvisoryADPContainer]**](AdvisoryADPContainer.md) |  | [optional] 
**cna** | [**AdvisoryCirclCna**](AdvisoryCirclCna.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_circl_containers import AdvisoryCirclContainers

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCirclContainers from a JSON string
advisory_circl_containers_instance = AdvisoryCirclContainers.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCirclContainers.to_json())

# convert the object into a dict
advisory_circl_containers_dict = advisory_circl_containers_instance.to_dict()
# create an instance of AdvisoryCirclContainers from a dict
advisory_circl_containers_from_dict = AdvisoryCirclContainers.from_dict(advisory_circl_containers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


