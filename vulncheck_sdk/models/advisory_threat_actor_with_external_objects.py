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
from vulncheck_sdk.models.advisory_cve_reference import AdvisoryCVEReference
from vulncheck_sdk.models.advisory_misp_value_no_id import AdvisoryMISPValueNoID
from vulncheck_sdk.models.advisory_mitre_attack_group_no_id import AdvisoryMITREAttackGroupNoID
from vulncheck_sdk.models.advisory_mitre_attack_tech_with_refs import AdvisoryMitreAttackTechWithRefs
from vulncheck_sdk.models.advisory_mitre_group_cti import AdvisoryMitreGroupCTI
from vulncheck_sdk.models.advisory_tool import AdvisoryTool
from vulncheck_sdk.models.advisory_vendor_name_for_threat_actor import AdvisoryVendorNameForThreatActor
from vulncheck_sdk.models.advisory_vendor_product import AdvisoryVendorProduct
from typing import Optional, Set
from typing_extensions import Self

class AdvisoryThreatActorWithExternalObjects(BaseModel):
    """
    AdvisoryThreatActorWithExternalObjects
    """ # noqa: E501
    associated_mitre_attack_techniques: Optional[List[AdvisoryMitreAttackTechWithRefs]] = None
    country: Optional[StrictStr] = None
    cve_references: Optional[List[AdvisoryCVEReference]] = None
    date_added: Optional[StrictStr] = None
    malpedia_url: Optional[StrictStr] = None
    misp_id: Optional[StrictStr] = None
    misp_threat_actor: Optional[AdvisoryMISPValueNoID] = None
    mitre_attack_group: Optional[AdvisoryMITREAttackGroupNoID] = None
    mitre_group_cti: Optional[AdvisoryMitreGroupCTI] = None
    mitre_id: Optional[StrictStr] = None
    threat_actor_name: Optional[StrictStr] = None
    tools: Optional[List[AdvisoryTool]] = None
    vendor_names_for_threat_actors: Optional[List[AdvisoryVendorNameForThreatActor]] = None
    vendors_and_products_targeted: Optional[List[AdvisoryVendorProduct]] = None
    __properties: ClassVar[List[str]] = ["associated_mitre_attack_techniques", "country", "cve_references", "date_added", "malpedia_url", "misp_id", "misp_threat_actor", "mitre_attack_group", "mitre_group_cti", "mitre_id", "threat_actor_name", "tools", "vendor_names_for_threat_actors", "vendors_and_products_targeted"]

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
        """Create an instance of AdvisoryThreatActorWithExternalObjects from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associated_mitre_attack_techniques (list)
        _items = []
        if self.associated_mitre_attack_techniques:
            for _item_associated_mitre_attack_techniques in self.associated_mitre_attack_techniques:
                if _item_associated_mitre_attack_techniques:
                    _items.append(_item_associated_mitre_attack_techniques.to_dict())
            _dict['associated_mitre_attack_techniques'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cve_references (list)
        _items = []
        if self.cve_references:
            for _item_cve_references in self.cve_references:
                if _item_cve_references:
                    _items.append(_item_cve_references.to_dict())
            _dict['cve_references'] = _items
        # override the default output from pydantic by calling `to_dict()` of misp_threat_actor
        if self.misp_threat_actor:
            _dict['misp_threat_actor'] = self.misp_threat_actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mitre_attack_group
        if self.mitre_attack_group:
            _dict['mitre_attack_group'] = self.mitre_attack_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mitre_group_cti
        if self.mitre_group_cti:
            _dict['mitre_group_cti'] = self.mitre_group_cti.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item_tools in self.tools:
                if _item_tools:
                    _items.append(_item_tools.to_dict())
            _dict['tools'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vendor_names_for_threat_actors (list)
        _items = []
        if self.vendor_names_for_threat_actors:
            for _item_vendor_names_for_threat_actors in self.vendor_names_for_threat_actors:
                if _item_vendor_names_for_threat_actors:
                    _items.append(_item_vendor_names_for_threat_actors.to_dict())
            _dict['vendor_names_for_threat_actors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vendors_and_products_targeted (list)
        _items = []
        if self.vendors_and_products_targeted:
            for _item_vendors_and_products_targeted in self.vendors_and_products_targeted:
                if _item_vendors_and_products_targeted:
                    _items.append(_item_vendors_and_products_targeted.to_dict())
            _dict['vendors_and_products_targeted'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvisoryThreatActorWithExternalObjects from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associated_mitre_attack_techniques": [AdvisoryMitreAttackTechWithRefs.from_dict(_item) for _item in obj["associated_mitre_attack_techniques"]] if obj.get("associated_mitre_attack_techniques") is not None else None,
            "country": obj.get("country"),
            "cve_references": [AdvisoryCVEReference.from_dict(_item) for _item in obj["cve_references"]] if obj.get("cve_references") is not None else None,
            "date_added": obj.get("date_added"),
            "malpedia_url": obj.get("malpedia_url"),
            "misp_id": obj.get("misp_id"),
            "misp_threat_actor": AdvisoryMISPValueNoID.from_dict(obj["misp_threat_actor"]) if obj.get("misp_threat_actor") is not None else None,
            "mitre_attack_group": AdvisoryMITREAttackGroupNoID.from_dict(obj["mitre_attack_group"]) if obj.get("mitre_attack_group") is not None else None,
            "mitre_group_cti": AdvisoryMitreGroupCTI.from_dict(obj["mitre_group_cti"]) if obj.get("mitre_group_cti") is not None else None,
            "mitre_id": obj.get("mitre_id"),
            "threat_actor_name": obj.get("threat_actor_name"),
            "tools": [AdvisoryTool.from_dict(_item) for _item in obj["tools"]] if obj.get("tools") is not None else None,
            "vendor_names_for_threat_actors": [AdvisoryVendorNameForThreatActor.from_dict(_item) for _item in obj["vendor_names_for_threat_actors"]] if obj.get("vendor_names_for_threat_actors") is not None else None,
            "vendors_and_products_targeted": [AdvisoryVendorProduct.from_dict(_item) for _item in obj["vendors_and_products_targeted"]] if obj.get("vendors_and_products_targeted") is not None else None
        })
        return _obj


