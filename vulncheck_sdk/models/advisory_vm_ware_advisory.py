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
from typing import Optional, Set
from typing_extensions import Self

class AdvisoryVMWareAdvisory(BaseModel):
    """
    AdvisoryVMWareAdvisory
    """ # noqa: E501
    advisory_id: Optional[StrictStr] = Field(default=None, alias="AdvisoryID")
    advisory_url: Optional[StrictStr] = Field(default=None, alias="AdvisoryURL")
    cvssv3_range: Optional[StrictStr] = Field(default=None, alias="CVSSv3Range")
    issue_date: Optional[StrictStr] = Field(default=None, alias="IssueDate")
    severity: Optional[StrictStr] = Field(default=None, alias="Severity")
    synopsis: Optional[StrictStr] = Field(default=None, alias="Synopsis")
    updated_on: Optional[StrictStr] = Field(default=None, alias="UpdatedOn")
    cve: Optional[List[StrictStr]] = None
    date_added: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["AdvisoryID", "AdvisoryURL", "CVSSv3Range", "IssueDate", "Severity", "Synopsis", "UpdatedOn", "cve", "date_added", "id", "updated_at"]

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
        """Create an instance of AdvisoryVMWareAdvisory from a JSON string"""
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
        """Create an instance of AdvisoryVMWareAdvisory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AdvisoryID": obj.get("AdvisoryID"),
            "AdvisoryURL": obj.get("AdvisoryURL"),
            "CVSSv3Range": obj.get("CVSSv3Range"),
            "IssueDate": obj.get("IssueDate"),
            "Severity": obj.get("Severity"),
            "Synopsis": obj.get("Synopsis"),
            "UpdatedOn": obj.get("UpdatedOn"),
            "cve": obj.get("cve"),
            "date_added": obj.get("date_added"),
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


