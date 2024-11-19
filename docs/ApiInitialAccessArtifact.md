# ApiInitialAccessArtifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_name** | **str** | ArtifactName is a title to associate with this artifact. | [optional] 
**artifacts_url** | **List[str]** | ArtifactsURL are URLs to the available artifact. | [optional] 
**censys_queries** | **List[str]** | CensysQueries are queries for examining potential Internet-exposed devices &amp; applications with Censys in URL form. | [optional] 
**censys_raw_queries** | **List[str]** | CensysRawQueries are raw queries for examining potential Internet-exposed devices &amp; applications with Censys. | [optional] 
**clone_sshurl** | **str** | CloneSSHURL is the git URL to clone the artifact with. | [optional] 
**date_added** | **str** | DateAdded is when this artifact entry was first added to the InitialAccess data set. | [optional] 
**exploit** | **bool** | Exploit indicates whether or not an exploit is available in this artifact. | [optional] 
**fofa_queries** | **List[str]** | FOFAQueries are raw queries for examining potential Internet-exposed devices &amp; applications with FOFA. | [optional] 
**greynoise_queries** | **List[str]** | GreynoiseQueries are queries for finding the vulnerability via honeypot data. | [optional] 
**nmap_script** | **bool** | NmapScript indicates whether or not an nmap script for scanning environment exists in this artifact. | [optional] 
**pcap** | **bool** | PCAP indicates whether of not a package capture of the exploit PoC exploiting a vulnerable system exists in this artifact. | [optional] 
**product** | **List[str]** | Product are the software that has the vulnerability. | [optional] 
**shodan_queries** | **List[str]** | ShodanQueries are queries for examining potential Internet-exposed devices &amp; applications with Shodan in URL form. | [optional] 
**shodan_raw_queries** | **List[str]** | ShodanRawQueries are raw queries for examining potential Internet-exposed devices &amp; applications with Shodan. | [optional] 
**snort_rule** | **bool** | SnortRule indicates whether or not a Snort rule designed to detect the exploitation of the vulnerability over the network exists in this artifact. | [optional] 
**suricata_rule** | **bool** | SuricataRule indicates whether or not a Suricata rule designed to detect the exploitation of the vulnerability over the network exists in this artifact. | [optional] 
**target_docker** | **bool** | TargetDocker indicates whether or not there is an available docker image with the vulnerability. | [optional] 
**target_service** | **str** | TargetService indicates the service (HTTP, FTP, etc) that this exploit targets. | [optional] 
**vendor** | **str** | Vendor of the vulnerable product | [optional] 
**version_scanner** | **bool** | VersionScanner indicates whether or not the exploit PoC can determine if target system is vulnerable without sending exploit payload in this artifact. | [optional] 
**yara** | **bool** | YARA indicates whether or not a YARA rule designed to detect the exploit on an endpoint exists in this artifact. | [optional] 
**zeroday** | **bool** | Zeroday indicates whether or not it is a VulnCheck zeroday. | [optional] 
**zoom_eye_queries** | **List[str]** | ZoomEyeQueries are raw queries for examining potential Internet-exposed devices &amp; applications with ZoomEye. | [optional] 

## Example

```python
from vulncheck_sdk.models.api_initial_access_artifact import ApiInitialAccessArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInitialAccessArtifact from a JSON string
api_initial_access_artifact_instance = ApiInitialAccessArtifact.from_json(json)
# print the JSON string representation of the object
print(ApiInitialAccessArtifact.to_json())

# convert the object into a dict
api_initial_access_artifact_dict = api_initial_access_artifact_instance.to_dict()
# create an instance of ApiInitialAccessArtifact from a dict
api_initial_access_artifact_from_dict = ApiInitialAccessArtifact.from_dict(api_initial_access_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


