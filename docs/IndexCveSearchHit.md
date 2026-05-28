# IndexCveSearchHit

index.CveSearchHit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the unique document identifier within the index. | [optional] 
**index** | **str** | Index is the name of the index where this document was found. | [optional] 
**score** | **float** | Score is the relevance score from OpenSearch (higher &#x3D; more relevant). | [optional] 
**source** | **object** | Source is the full document content. Structure varies by index. | [optional] 

## Example

```python
from vulncheck_sdk.models.index_cve_search_hit import IndexCveSearchHit

# TODO update the JSON string below
json = "{}"
# create an instance of IndexCveSearchHit from a JSON string
index_cve_search_hit_instance = IndexCveSearchHit.from_json(json)
# print the JSON string representation of the object
print(IndexCveSearchHit.to_json())

# convert the object into a dict
index_cve_search_hit_dict = index_cve_search_hit_instance.to_dict()
# create an instance of IndexCveSearchHit from a dict
index_cve_search_hit_from_dict = IndexCveSearchHit.from_dict(index_cve_search_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


