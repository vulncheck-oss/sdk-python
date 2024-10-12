# AdvisoryBDUAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bdu_id** | **str** | BDU:2022-03833 | [optional] 
**cve** | **List[str]** | []string{\&quot;CVE-2022-28194\&quot;} | [optional] 
**cvss** | [**AdvisoryBDUCvss**](AdvisoryBDUCvss.md) |  | [optional] 
**cvss3** | [**AdvisoryBDUCvss3**](AdvisoryBDUCvss3.md) |  | [optional] 
**cwe** | **str** | CWE-119 | [optional] 
**date_added** | **str** |  | [optional] 
**description_ru** | **str** | Библиотека libxml2 до версии 2.9.12 не корректно обрабатывает XML-документы, содержащие определенные сущности. В результате могут быть выполнены произвольные команды. | [optional] 
**environment** | [**AdvisoryBDUEnvironment**](AdvisoryBDUEnvironment.md) |  | [optional] 
**exploit_status_en** | **str** | Exploited | [optional] 
**exploit_status_ru** | **str** | Exploited | [optional] 
**fix_status_en** | **str** | Fixed | [optional] 
**fix_status_ru** | **str** | Fixed | [optional] 
**identify_date** | **str** | 2022-09-01 | [optional] 
**name_ru** | **str** | BDU:2022-03833: Уязвимость модуля Cboot (tegrabl_cbo.c) пакета драйверов микропрограммного обеспечения вычислительных плат NVIDIA Jetson, позволяющая нарушителю выполнить произвольный код или вызвать частичный отказ в обслуживании | [optional] 
**severity_ru** | **str** | High | [optional] 
**solution_ru** | **str** | Обновите драйверы микропрограммного обеспечения вычислительных плат NVIDIA Jetson до версии 32.6.1 или более поздней | [optional] 
**sources** | **List[str]** | https://nvd.nist.gov/vuln/detail/CVE-2022-28194 | [optional] 
**text_ru** | **str** | Библиотека libxml2 до версии 2.9.12 не корректно обрабатывает XML-документы, содержащие определенные сущности. В результате могут быть выполнены произвольные команды. | [optional] 
**url** | **str** | https://bdu.fstec.ru/vul/2022-03833 | [optional] 
**vul_status_en** | **str** | Exploitable | [optional] 
**vul_status_ru** | **str** | Exploitable | [optional] 
**vulnerable_software** | [**AdvisoryBDUVulnerableSoftware**](AdvisoryBDUVulnerableSoftware.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bdu_advisory import AdvisoryBDUAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBDUAdvisory from a JSON string
advisory_bdu_advisory_instance = AdvisoryBDUAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBDUAdvisory.to_json())

# convert the object into a dict
advisory_bdu_advisory_dict = advisory_bdu_advisory_instance.to_dict()
# create an instance of AdvisoryBDUAdvisory from a dict
advisory_bdu_advisory_from_dict = AdvisoryBDUAdvisory.from_dict(advisory_bdu_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


