# AdvisorySiemensPublisher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**contact_details** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_publisher import AdvisorySiemensPublisher

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensPublisher from a JSON string
advisory_siemens_publisher_instance = AdvisorySiemensPublisher.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensPublisher.to_json())

# convert the object into a dict
advisory_siemens_publisher_dict = advisory_siemens_publisher_instance.to_dict()
# create an instance of AdvisorySiemensPublisher from a dict
advisory_siemens_publisher_from_dict = AdvisorySiemensPublisher.from_dict(advisory_siemens_publisher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


