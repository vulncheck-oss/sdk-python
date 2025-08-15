# AdvisoryDFNCert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary_de** | **str** |  | [optional] 
**title_de** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_dfn_cert import AdvisoryDFNCert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDFNCert from a JSON string
advisory_dfn_cert_instance = AdvisoryDFNCert.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDFNCert.to_json())

# convert the object into a dict
advisory_dfn_cert_dict = advisory_dfn_cert_instance.to_dict()
# create an instance of AdvisoryDFNCert from a dict
advisory_dfn_cert_from_dict = AdvisoryDFNCert.from_dict(advisory_dfn_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


