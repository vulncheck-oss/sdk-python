# AdvisorySiemensProductStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**known_affected** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_product_status import AdvisorySiemensProductStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensProductStatus from a JSON string
advisory_siemens_product_status_instance = AdvisorySiemensProductStatus.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensProductStatus.to_json())

# convert the object into a dict
advisory_siemens_product_status_dict = advisory_siemens_product_status_instance.to_dict()
# create an instance of AdvisorySiemensProductStatus from a dict
advisory_siemens_product_status_from_dict = AdvisorySiemensProductStatus.from_dict(advisory_siemens_product_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


