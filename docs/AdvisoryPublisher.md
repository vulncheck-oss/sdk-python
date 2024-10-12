# AdvisoryPublisher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**contact_details** | **str** |  | [optional] 
**issuing_authority** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_publisher import AdvisoryPublisher

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPublisher from a JSON string
advisory_publisher_instance = AdvisoryPublisher.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPublisher.to_json())

# convert the object into a dict
advisory_publisher_dict = advisory_publisher_instance.to_dict()
# create an instance of AdvisoryPublisher from a dict
advisory_publisher_from_dict = AdvisoryPublisher.from_dict(advisory_publisher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


