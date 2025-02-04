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
from vulncheck_sdk.models.advisory_prime_version import AdvisoryPrimeVersion
from vulncheck_sdk.models.advisory_zulu_version import AdvisoryZuluVersion
from typing import Optional, Set
from typing_extensions import Self

class AdvisoryAzul(BaseModel):
    """
    AdvisoryAzul
    """ # noqa: E501
    base_score: Optional[StrictStr] = None
    cve: Optional[List[StrictStr]] = None
    date_added: Optional[StrictStr] = None
    prime_version: Optional[List[AdvisoryPrimeVersion]] = None
    release: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    zulu_version: Optional[List[AdvisoryZuluVersion]] = None
    __properties: ClassVar[List[str]] = ["base_score", "cve", "date_added", "prime_version", "release", "url", "zulu_version"]

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
        """Create an instance of AdvisoryAzul from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in prime_version (list)
        _items = []
        if self.prime_version:
            for _item_prime_version in self.prime_version:
                if _item_prime_version:
                    _items.append(_item_prime_version.to_dict())
            _dict['prime_version'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zulu_version (list)
        _items = []
        if self.zulu_version:
            for _item_zulu_version in self.zulu_version:
                if _item_zulu_version:
                    _items.append(_item_zulu_version.to_dict())
            _dict['zulu_version'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvisoryAzul from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "base_score": obj.get("base_score"),
            "cve": obj.get("cve"),
            "date_added": obj.get("date_added"),
            "prime_version": [AdvisoryPrimeVersion.from_dict(_item) for _item in obj["prime_version"]] if obj.get("prime_version") is not None else None,
            "release": obj.get("release"),
            "url": obj.get("url"),
            "zulu_version": [AdvisoryZuluVersion.from_dict(_item) for _item in obj["zulu_version"]] if obj.get("zulu_version") is not None else None
        })
        return _obj


