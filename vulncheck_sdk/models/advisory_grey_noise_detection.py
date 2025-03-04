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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from vulncheck_sdk.models.advisory_grey_noise_tags import AdvisoryGreyNoiseTags
from typing import Optional, Set
from typing_extensions import Self

class AdvisoryGreyNoiseDetection(BaseModel):
    """
    AdvisoryGreyNoiseDetection
    """ # noqa: E501
    category: Optional[StrictStr] = None
    cve: Optional[List[StrictStr]] = None
    date_added: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    intention: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    recommend_block: Optional[StrictBool] = None
    references: Optional[List[StrictStr]] = None
    related_tags: Optional[List[AdvisoryGreyNoiseTags]] = None
    slug: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["category", "cve", "date_added", "description", "id", "intention", "label", "name", "recommend_block", "references", "related_tags", "slug", "url"]

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
        """Create an instance of AdvisoryGreyNoiseDetection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in related_tags (list)
        _items = []
        if self.related_tags:
            for _item_related_tags in self.related_tags:
                if _item_related_tags:
                    _items.append(_item_related_tags.to_dict())
            _dict['related_tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvisoryGreyNoiseDetection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "cve": obj.get("cve"),
            "date_added": obj.get("date_added"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "intention": obj.get("intention"),
            "label": obj.get("label"),
            "name": obj.get("name"),
            "recommend_block": obj.get("recommend_block"),
            "references": obj.get("references"),
            "related_tags": [AdvisoryGreyNoiseTags.from_dict(_item) for _item in obj["related_tags"]] if obj.get("related_tags") is not None else None,
            "slug": obj.get("slug"),
            "url": obj.get("url")
        })
        return _obj


