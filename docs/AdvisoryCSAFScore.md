# AdvisoryCSAFScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_v2** | [**AdvisoryCVSSV2**](AdvisoryCVSSV2.md) |  | [optional] 
**cvss_v3** | [**AdvisoryCVSSV3**](AdvisoryCVSSV3.md) |  | [optional] 
**products** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_csaf_score import AdvisoryCSAFScore

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCSAFScore from a JSON string
advisory_csaf_score_instance = AdvisoryCSAFScore.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCSAFScore.to_json())

# convert the object into a dict
advisory_csaf_score_dict = advisory_csaf_score_instance.to_dict()
# create an instance of AdvisoryCSAFScore from a dict
advisory_csaf_score_from_dict = AdvisoryCSAFScore.from_dict(advisory_csaf_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


