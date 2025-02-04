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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiCPE(BaseModel):
    """
    ApiCPE
    """ # noqa: E501
    edition: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    other: Optional[StrictStr] = None
    part: Optional[StrictStr] = None
    product: Optional[StrictStr] = None
    sw_edition: Optional[StrictStr] = None
    target_hw: Optional[StrictStr] = None
    target_sw: Optional[StrictStr] = None
    update: Optional[StrictStr] = None
    vendor: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["edition", "language", "other", "part", "product", "sw_edition", "target_hw", "target_sw", "update", "vendor", "version"]

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
        """Create an instance of ApiCPE from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiCPE from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "edition": obj.get("edition"),
            "language": obj.get("language"),
            "other": obj.get("other"),
            "part": obj.get("part"),
            "product": obj.get("product"),
            "sw_edition": obj.get("sw_edition"),
            "target_hw": obj.get("target_hw"),
            "target_sw": obj.get("target_sw"),
            "update": obj.get("update"),
            "vendor": obj.get("vendor"),
            "version": obj.get("version")
        })
        return _obj


