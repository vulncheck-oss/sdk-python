# AdvisoryBDUVulnerableSoftware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**soft** | [**AdvisoryBDUSoft**](AdvisoryBDUSoft.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bdu_vulnerable_software import AdvisoryBDUVulnerableSoftware

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUVulnerableSoftware from a JSON string
advisory_bdu_vulnerable_software_instance = AdvisoryBDUVulnerableSoftware.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUVulnerableSoftware.to_json())

# convert the object into a dict
advisory_bdu_vulnerable_software_dict = advisory_bdu_vulnerable_software_instance.to_dict()
# create an instance of AdvisoryBDUVulnerableSoftware from a dict
advisory_bdu_vulnerable_software_from_dict = AdvisoryBDUVulnerableSoftware.from_dict(advisory_bdu_vulnerable_software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


