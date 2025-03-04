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
from vulncheck_sdk.models.advisory_m_containers import AdvisoryMContainers
from vulncheck_sdk.models.advisory_m_cve_metadata import AdvisoryMCveMetadata
from typing import Optional, Set
from typing_extensions import Self

class AdvisoryMitreCVEListV5Ref(BaseModel):
    """
    AdvisoryMitreCVEListV5Ref
    """ # noqa: E501
    containers: Optional[AdvisoryMContainers] = None
    cve_metadata: Optional[AdvisoryMCveMetadata] = Field(default=None, alias="cveMetadata")
    data_type: Optional[StrictStr] = Field(default=None, alias="dataType")
    data_version: Optional[StrictStr] = Field(default=None, alias="dataVersion")
    __properties: ClassVar[List[str]] = ["containers", "cveMetadata", "dataType", "dataVersion"]

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
        """Create an instance of AdvisoryMitreCVEListV5Ref from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of containers
        if self.containers:
            _dict['containers'] = self.containers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cve_metadata
        if self.cve_metadata:
            _dict['cveMetadata'] = self.cve_metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvisoryMitreCVEListV5Ref from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "containers": AdvisoryMContainers.from_dict(obj["containers"]) if obj.get("containers") is not None else None,
            "cveMetadata": AdvisoryMCveMetadata.from_dict(obj["cveMetadata"]) if obj.get("cveMetadata") is not None else None,
            "dataType": obj.get("dataType"),
            "dataVersion": obj.get("dataVersion")
        })
        return _obj


