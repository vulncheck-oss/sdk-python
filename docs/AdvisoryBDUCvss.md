# AdvisoryBDUCvss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector** | [**AdvisoryBDUVector**](AdvisoryBDUVector.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bdu_cvss import AdvisoryBDUCvss

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUCvss from a JSON string
advisory_bdu_cvss_instance = AdvisoryBDUCvss.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUCvss.to_json())

# convert the object into a dict
advisory_bdu_cvss_dict = advisory_bdu_cvss_instance.to_dict()
# create an instance of AdvisoryBDUCvss from a dict
advisory_bdu_cvss_from_dict = AdvisoryBDUCvss.from_dict(advisory_bdu_cvss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


