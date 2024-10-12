# AdvisoryAdobeAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_adobe_affected import AdvisoryAdobeAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAdobeAffected from a JSON string
advisory_adobe_affected_instance = AdvisoryAdobeAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAdobeAffected.to_json())

# convert the object into a dict
advisory_adobe_affected_dict = advisory_adobe_affected_instance.to_dict()
# create an instance of AdvisoryAdobeAffected from a dict
advisory_adobe_affected_from_dict = AdvisoryAdobeAffected.from_dict(advisory_adobe_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


