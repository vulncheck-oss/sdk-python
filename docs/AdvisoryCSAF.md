# AdvisoryCSAF


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**AdvisoryDocumentMetadata**](AdvisoryDocumentMetadata.md) | Document contains metadata about the CSAF document itself.  https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#321-document-property | [optional] 
**notes** | [**List[AdvisoryCSAFNote]**](AdvisoryCSAFNote.md) | Notes holds notes associated with the whole document. https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#3217-document-property---notes | [optional] 
**product_tree** | [**AdvisoryProductBranch**](AdvisoryProductBranch.md) | ProductTree contains information about the product tree (branches only).  https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#322-product-tree-property | [optional] 
**vulnerabilities** | [**List[AdvisoryCSAFVulnerability]**](AdvisoryCSAFVulnerability.md) | Vulnerabilities contains information about the vulnerabilities, (i.e. CVEs), associated threats, and product status.  https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#323-vulnerabilities-property | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_csaf import AdvisoryCSAF

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCSAF from a JSON string
advisory_csaf_instance = AdvisoryCSAF.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCSAF.to_json())

# convert the object into a dict
advisory_csaf_dict = advisory_csaf_instance.to_dict()
# create an instance of AdvisoryCSAF from a dict
advisory_csaf_from_dict = AdvisoryCSAF.from_dict(advisory_csaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


