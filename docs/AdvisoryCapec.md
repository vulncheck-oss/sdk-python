# AdvisoryCapec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capec_id** | **str** |  | [optional] 
**capec_name** | **str** |  | [optional] 
**capec_url** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_capec import AdvisoryCapec

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCapec from a JSON string
advisory_capec_instance = AdvisoryCapec.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCapec.to_json())

# convert the object into a dict
advisory_capec_dict = advisory_capec_instance.to_dict()
# create an instance of AdvisoryCapec from a dict
advisory_capec_from_dict = AdvisoryCapec.from_dict(advisory_capec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


