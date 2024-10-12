# AdvisoryIstio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_version** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_istio import AdvisoryIstio

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIstio from a JSON string
advisory_istio_instance = AdvisoryIstio.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIstio.to_json())

# convert the object into a dict
advisory_istio_dict = advisory_istio_instance.to_dict()
# create an instance of AdvisoryIstio from a dict
advisory_istio_from_dict = AdvisoryIstio.from_dict(advisory_istio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


