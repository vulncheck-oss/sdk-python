# AdvisoryBeckmanCoulter


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
from vulncheck_sdk.models.advisory_beckman_coulter import AdvisoryBeckmanCoulter

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBeckmanCoulter from a JSON string
advisory_beckman_coulter_instance = AdvisoryBeckmanCoulter.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBeckmanCoulter.to_json())

# convert the object into a dict
advisory_beckman_coulter_dict = advisory_beckman_coulter_instance.to_dict()
# create an instance of AdvisoryBeckmanCoulter from a dict
advisory_beckman_coulter_from_dict = AdvisoryBeckmanCoulter.from_dict(advisory_beckman_coulter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


