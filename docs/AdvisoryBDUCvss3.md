# AdvisoryBDUCvss3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector** | [**AdvisoryBDUVector**](AdvisoryBDUVector.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bdu_cvss3 import AdvisoryBDUCvss3

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUCvss3 from a JSON string
advisory_bdu_cvss3_instance = AdvisoryBDUCvss3.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUCvss3.to_json())

# convert the object into a dict
advisory_bdu_cvss3_dict = advisory_bdu_cvss3_instance.to_dict()
# create an instance of AdvisoryBDUCvss3 from a dict
advisory_bdu_cvss3_from_dict = AdvisoryBDUCvss3.from_dict(advisory_bdu_cvss3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


