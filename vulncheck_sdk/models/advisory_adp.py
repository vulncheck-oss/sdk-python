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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from vulncheck_sdk.models.advisory_m_affected import AdvisoryMAffected
from vulncheck_sdk.models.advisory_m_provider_metadata import AdvisoryMProviderMetadata
from vulncheck_sdk.models.advisory_vulnrichment_metric import AdvisoryVulnrichmentMetric
from typing import Optional, Set
from typing_extensions import Self

class AdvisoryADP(BaseModel):
    """
    AdvisoryADP
    """ # noqa: E501
    affected: Optional[List[AdvisoryMAffected]] = None
    metrics: Optional[List[AdvisoryVulnrichmentMetric]] = None
    provider_metadata: Optional[AdvisoryMProviderMetadata] = Field(default=None, alias="providerMetadata")
    __properties: ClassVar[List[str]] = ["affected", "metrics", "providerMetadata"]

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
        """Create an instance of AdvisoryADP from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in affected (list)
        _items = []
        if self.affected:
            for _item_affected in self.affected:
                if _item_affected:
                    _items.append(_item_affected.to_dict())
            _dict['affected'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item_metrics in self.metrics:
                if _item_metrics:
                    _items.append(_item_metrics.to_dict())
            _dict['metrics'] = _items
        # override the default output from pydantic by calling `to_dict()` of provider_metadata
        if self.provider_metadata:
            _dict['providerMetadata'] = self.provider_metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvisoryADP from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "affected": [AdvisoryMAffected.from_dict(_item) for _item in obj["affected"]] if obj.get("affected") is not None else None,
            "metrics": [AdvisoryVulnrichmentMetric.from_dict(_item) for _item in obj["metrics"]] if obj.get("metrics") is not None else None,
            "providerMetadata": AdvisoryMProviderMetadata.from_dict(obj["providerMetadata"]) if obj.get("providerMetadata") is not None else None
        })
        return _obj


