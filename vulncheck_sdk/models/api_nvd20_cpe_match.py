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
from vulncheck_sdk.models.api_nvd20_cpe_name import ApiNVD20CPEName
from typing import Optional, Set
from typing_extensions import Self

class ApiNVD20CPEMatch(BaseModel):
    """
    ApiNVD20CPEMatch
    """ # noqa: E501
    cpe_last_modified: Optional[StrictStr] = Field(default=None, alias="cpeLastModified")
    created: Optional[StrictStr] = None
    criteria: Optional[StrictStr] = None
    last_modified: Optional[StrictStr] = Field(default=None, alias="lastModified")
    match_criteria_id: Optional[StrictStr] = Field(default=None, alias="matchCriteriaId")
    matches: Optional[List[ApiNVD20CPEName]] = None
    status: Optional[StrictStr] = None
    version_end_excluding: Optional[StrictStr] = Field(default=None, alias="versionEndExcluding")
    version_end_including: Optional[StrictStr] = Field(default=None, alias="versionEndIncluding")
    version_start_excluding: Optional[StrictStr] = Field(default=None, alias="versionStartExcluding")
    version_start_including: Optional[StrictStr] = Field(default=None, alias="versionStartIncluding")
    __properties: ClassVar[List[str]] = ["cpeLastModified", "created", "criteria", "lastModified", "matchCriteriaId", "matches", "status", "versionEndExcluding", "versionEndIncluding", "versionStartExcluding", "versionStartIncluding"]

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
        """Create an instance of ApiNVD20CPEMatch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in matches (list)
        _items = []
        if self.matches:
            for _item_matches in self.matches:
                if _item_matches:
                    _items.append(_item_matches.to_dict())
            _dict['matches'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiNVD20CPEMatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpeLastModified": obj.get("cpeLastModified"),
            "created": obj.get("created"),
            "criteria": obj.get("criteria"),
            "lastModified": obj.get("lastModified"),
            "matchCriteriaId": obj.get("matchCriteriaId"),
            "matches": [ApiNVD20CPEName.from_dict(_item) for _item in obj["matches"]] if obj.get("matches") is not None else None,
            "status": obj.get("status"),
            "versionEndExcluding": obj.get("versionEndExcluding"),
            "versionEndIncluding": obj.get("versionEndIncluding"),
            "versionStartExcluding": obj.get("versionStartExcluding"),
            "versionStartIncluding": obj.get("versionStartIncluding")
        })
        return _obj


