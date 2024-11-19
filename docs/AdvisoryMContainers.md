# AdvisoryMContainers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adp** | [**List[AdvisoryADPContainer]**](AdvisoryADPContainer.md) |  | [optional] 
**cna** | [**AdvisoryMCna**](AdvisoryMCna.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_containers import AdvisoryMContainers

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMContainers from a JSON string
advisory_m_containers_instance = AdvisoryMContainers.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMContainers.to_json())

# convert the object into a dict
advisory_m_containers_dict = advisory_m_containers_instance.to_dict()
# create an instance of AdvisoryMContainers from a dict
advisory_m_containers_from_dict = AdvisoryMContainers.from_dict(advisory_m_containers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


