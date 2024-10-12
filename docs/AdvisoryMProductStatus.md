# AdvisoryMProductStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **List[str]** |  | [optional] 
**type** | **int** | diff | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_product_status import AdvisoryMProductStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMProductStatus from a JSON string
advisory_m_product_status_instance = AdvisoryMProductStatus.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMProductStatus.to_json())

# convert the object into a dict
advisory_m_product_status_dict = advisory_m_product_status_instance.to_dict()
# create an instance of AdvisoryMProductStatus from a dict
advisory_m_product_status_from_dict = AdvisoryMProductStatus.from_dict(advisory_m_product_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


