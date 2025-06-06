# coding: utf-8

"""
    VulnCheck API

    Version 3 of the VulnCheck API

    The version of the OpenAPI document: 3.0
    Contact: support@vulncheck.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from vulncheck_sdk.models.advisory_bdu_cvss import AdvisoryBDUCvss
from vulncheck_sdk.models.advisory_bdu_cvss3 import AdvisoryBDUCvss3
from vulncheck_sdk.models.advisory_bdu_environment import AdvisoryBDUEnvironment
from vulncheck_sdk.models.advisory_bdu_vulnerable_software import AdvisoryBDUVulnerableSoftware
from typing import Optional, Set
from typing_extensions import Self

class AdvisoryBDUAdvisory(BaseModel):
    """
    AdvisoryBDUAdvisory
    """ # noqa: E501
    bdu_id: Optional[StrictStr] = Field(default=None, description="BDU:2022-03833")
    cve: Optional[List[StrictStr]] = Field(default=None, description="[]string{\"CVE-2022-28194\"}")
    cvss: Optional[AdvisoryBDUCvss] = None
    cvss3: Optional[AdvisoryBDUCvss3] = None
    cwe: Optional[StrictStr] = Field(default=None, description="CWE-119")
    date_added: Optional[StrictStr] = None
    description_ru: Optional[StrictStr] = Field(default=None, description="Библиотека libxml2 до версии 2.9.12 не корректно обрабатывает XML-документы, содержащие определенные сущности. В результате могут быть выполнены произвольные команды.")
    environment: Optional[AdvisoryBDUEnvironment] = None
    exploit_status_en: Optional[StrictStr] = Field(default=None, description="Exploited")
    exploit_status_ru: Optional[StrictStr] = Field(default=None, description="Exploited")
    fix_status_en: Optional[StrictStr] = Field(default=None, description="Fixed")
    fix_status_ru: Optional[StrictStr] = Field(default=None, description="Fixed")
    identify_date: Optional[StrictStr] = Field(default=None, description="2022-09-01")
    name_ru: Optional[StrictStr] = Field(default=None, description="BDU:2022-03833: Уязвимость модуля Cboot (tegrabl_cbo.c) пакета драйверов микропрограммного обеспечения вычислительных плат NVIDIA Jetson, позволяющая нарушителю выполнить произвольный код или вызвать частичный отказ в обслуживании")
    severity_ru: Optional[StrictStr] = Field(default=None, description="High")
    solution_ru: Optional[StrictStr] = Field(default=None, description="Обновите драйверы микропрограммного обеспечения вычислительных плат NVIDIA Jetson до версии 32.6.1 или более поздней")
    sources: Optional[List[StrictStr]] = Field(default=None, description="https://nvd.nist.gov/vuln/detail/CVE-2022-28194")
    text_ru: Optional[StrictStr] = Field(default=None, description="Библиотека libxml2 до версии 2.9.12 не корректно обрабатывает XML-документы, содержащие определенные сущности. В результате могут быть выполнены произвольные команды.")
    url: Optional[StrictStr] = Field(default=None, description="https://bdu.fstec.ru/vul/2022-03833")
    vul_status_en: Optional[StrictStr] = Field(default=None, description="Exploitable")
    vul_status_ru: Optional[StrictStr] = Field(default=None, description="Exploitable")
    vulnerable_software: Optional[AdvisoryBDUVulnerableSoftware] = None
    __properties: ClassVar[List[str]] = ["bdu_id", "cve", "cvss", "cvss3", "cwe", "date_added", "description_ru", "environment", "exploit_status_en", "exploit_status_ru", "fix_status_en", "fix_status_ru", "identify_date", "name_ru", "severity_ru", "solution_ru", "sources", "text_ru", "url", "vul_status_en", "vul_status_ru", "vulnerable_software"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AdvisoryBDUAdvisory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cvss
        if self.cvss:
            _dict['cvss'] = self.cvss.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cvss3
        if self.cvss3:
            _dict['cvss3'] = self.cvss3.to_dict()
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict['environment'] = self.environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vulnerable_software
        if self.vulnerable_software:
            _dict['vulnerable_software'] = self.vulnerable_software.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvisoryBDUAdvisory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bdu_id": obj.get("bdu_id"),
            "cve": obj.get("cve"),
            "cvss": AdvisoryBDUCvss.from_dict(obj["cvss"]) if obj.get("cvss") is not None else None,
            "cvss3": AdvisoryBDUCvss3.from_dict(obj["cvss3"]) if obj.get("cvss3") is not None else None,
            "cwe": obj.get("cwe"),
            "date_added": obj.get("date_added"),
            "description_ru": obj.get("description_ru"),
            "environment": AdvisoryBDUEnvironment.from_dict(obj["environment"]) if obj.get("environment") is not None else None,
            "exploit_status_en": obj.get("exploit_status_en"),
            "exploit_status_ru": obj.get("exploit_status_ru"),
            "fix_status_en": obj.get("fix_status_en"),
            "fix_status_ru": obj.get("fix_status_ru"),
            "identify_date": obj.get("identify_date"),
            "name_ru": obj.get("name_ru"),
            "severity_ru": obj.get("severity_ru"),
            "solution_ru": obj.get("solution_ru"),
            "sources": obj.get("sources"),
            "text_ru": obj.get("text_ru"),
            "url": obj.get("url"),
            "vul_status_en": obj.get("vul_status_en"),
            "vul_status_ru": obj.get("vul_status_ru"),
            "vulnerable_software": AdvisoryBDUVulnerableSoftware.from_dict(obj["vulnerable_software"]) if obj.get("vulnerable_software") is not None else None
        })
        return _obj


