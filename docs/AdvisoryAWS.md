# AdvisoryAWS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_aws import AdvisoryAWS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAWS from a JSON string
advisory_aws_instance = AdvisoryAWS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAWS.to_json())

# convert the object into a dict
advisory_aws_dict = advisory_aws_instance.to_dict()
# create an instance of AdvisoryAWS from a dict
advisory_aws_from_dict = AdvisoryAWS.from_dict(advisory_aws_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


