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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from vulncheck_sdk.models.api_cpe_name import ApiCPEName
from typing import Optional, Set
from typing_extensions import Self

class ApiCPEMatch(BaseModel):
    """
    ApiCPEMatch
    """ # noqa: E501
    cpe22_uri: Optional[StrictStr] = Field(default=None, alias="cpe22Uri")
    cpe23_uri: Optional[StrictStr] = Field(default=None, alias="cpe23Uri")
    cpe_name: Optional[List[ApiCPEName]] = None
    version_end_excluding: Optional[StrictStr] = Field(default=None, alias="versionEndExcluding")
    version_end_including: Optional[StrictStr] = Field(default=None, alias="versionEndIncluding")
    version_start_excluding: Optional[StrictStr] = Field(default=None, alias="versionStartExcluding")
    version_start_including: Optional[StrictStr] = Field(default=None, alias="versionStartIncluding")
    vulnerable: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["cpe22Uri", "cpe23Uri", "cpe_name", "versionEndExcluding", "versionEndIncluding", "versionStartExcluding", "versionStartIncluding", "vulnerable"]

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
        """Create an instance of ApiCPEMatch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cpe_name (list)
        _items = []
        if self.cpe_name:
            for _item_cpe_name in self.cpe_name:
                if _item_cpe_name:
                    _items.append(_item_cpe_name.to_dict())
            _dict['cpe_name'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiCPEMatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpe22Uri": obj.get("cpe22Uri"),
            "cpe23Uri": obj.get("cpe23Uri"),
            "cpe_name": [ApiCPEName.from_dict(_item) for _item in obj["cpe_name"]] if obj.get("cpe_name") is not None else None,
            "versionEndExcluding": obj.get("versionEndExcluding"),
            "versionEndIncluding": obj.get("versionEndIncluding"),
            "versionStartExcluding": obj.get("versionStartExcluding"),
            "versionStartIncluding": obj.get("versionStartIncluding"),
            "vulnerable": obj.get("vulnerable")
        })
        return _obj


