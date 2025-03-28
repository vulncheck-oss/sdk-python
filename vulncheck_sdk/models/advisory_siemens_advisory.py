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
from vulncheck_sdk.models.advisory_ssa_source import AdvisorySSASource
from typing import Optional, Set
from typing_extensions import Self

class AdvisorySiemensAdvisory(BaseModel):
    """
    AdvisorySiemensAdvisory
    """ # noqa: E501
    csaf_url: Optional[StrictStr] = None
    cve: Optional[List[StrictStr]] = None
    cvrf_url: Optional[StrictStr] = None
    date_added: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    last_update: Optional[StrictStr] = Field(default=None, description="could potentially kill this in the future as it's a dupe")
    pdf_url: Optional[StrictStr] = None
    products: Optional[List[StrictStr]] = None
    ssa: Optional[AdvisorySSASource] = None
    tags: Optional[List[StrictStr]] = None
    title: Optional[StrictStr] = None
    txt_url: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["csaf_url", "cve", "cvrf_url", "date_added", "html_url", "id", "last_update", "pdf_url", "products", "ssa", "tags", "title", "txt_url", "updated_at"]

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
        """Create an instance of AdvisorySiemensAdvisory from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ssa
        if self.ssa:
            _dict['ssa'] = self.ssa.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvisorySiemensAdvisory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "csaf_url": obj.get("csaf_url"),
            "cve": obj.get("cve"),
            "cvrf_url": obj.get("cvrf_url"),
            "date_added": obj.get("date_added"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "last_update": obj.get("last_update"),
            "pdf_url": obj.get("pdf_url"),
            "products": obj.get("products"),
            "ssa": AdvisorySSASource.from_dict(obj["ssa"]) if obj.get("ssa") is not None else None,
            "tags": obj.get("tags"),
            "title": obj.get("title"),
            "txt_url": obj.get("txt_url"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


