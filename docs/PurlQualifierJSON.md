# PurlQualifierJSON


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.purl_qualifier_json import PurlQualifierJSON

# TODO update the JSON string below
json = "{}"
# create an instance of PurlQualifierJSON from a JSON string
purl_qualifier_json_instance = PurlQualifierJSON.from_json(json)
# print the JSON string representation of the object
print(PurlQualifierJSON.to_json())

# convert the object into a dict
purl_qualifier_json_dict = purl_qualifier_json_instance.to_dict()
# create an instance of PurlQualifierJSON from a dict
purl_qualifier_json_from_dict = PurlQualifierJSON.from_dict(purl_qualifier_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


