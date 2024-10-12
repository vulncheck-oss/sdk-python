# AdvisoryAusCert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**publisher** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_aus_cert import AdvisoryAusCert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAusCert from a JSON string
advisory_aus_cert_instance = AdvisoryAusCert.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAusCert.to_json())

# convert the object into a dict
advisory_aus_cert_dict = advisory_aus_cert_instance.to_dict()
# create an instance of AdvisoryAusCert from a dict
advisory_aus_cert_from_dict = AdvisoryAusCert.from_dict(advisory_aus_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


