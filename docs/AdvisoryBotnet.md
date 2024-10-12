# AdvisoryBotnet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**botnet_name** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cve_references** | [**List[AdvisoryCVEReference]**](AdvisoryCVEReference.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**malpedia_url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_botnet import AdvisoryBotnet

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBotnet from a JSON string
advisory_botnet_instance = AdvisoryBotnet.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBotnet.to_json())

# convert the object into a dict
advisory_botnet_dict = advisory_botnet_instance.to_dict()
# create an instance of AdvisoryBotnet from a dict
advisory_botnet_from_dict = AdvisoryBotnet.from_dict(advisory_botnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


