# coding: utf-8

"""
    VulnCheck API

    Version 3 of the VulnCheck API

    The version of the OpenAPI document: 3.0
    Contact: support@vulncheck.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from vulncheck_sdk.models.api_impact_extended import ApiImpactExtended

class TestApiImpactExtended(unittest.TestCase):
    """ApiImpactExtended unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiImpactExtended:
        """Test ApiImpactExtended
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiImpactExtended`
        """
        model = ApiImpactExtended()
        if include_optional:
            return ApiImpactExtended(
                base_metric_v2 = vulncheck_sdk.models.api/base_metric_v2.api.BaseMetricV2(
                    ac_insuf_info = True, 
                    cvss_v2 = vulncheck_sdk.models.api/cvssv2.api.CVSSV2(
                        access_complexity = '', 
                        access_vector = '', 
                        authentication = '', 
                        availability_impact = '', 
                        base_score = 1.337, 
                        confidentiality_impact = '', 
                        integrity_impact = '', 
                        vector_string = '', 
                        version = '', ), 
                    exploitability_score = 1.337, 
                    impact_score = 1.337, 
                    obtain_all_privilege = True, 
                    obtain_other_privilege = True, 
                    obtain_user_privilege = True, 
                    severity = '', 
                    user_interaction_required = True, ),
                base_metric_v3 = vulncheck_sdk.models.api/base_metric_v3.api.BaseMetricV3(
                    cvss_v3 = vulncheck_sdk.models.api/cvssv3.api.CVSSV3(
                        attack_complexity = '', 
                        attack_vector = '', 
                        availability_impact = '', 
                        base_score = 1.337, 
                        base_severity = '', 
                        confidentiality_impact = '', 
                        integrity_impact = '', 
                        privileges_required = '', 
                        scope = '', 
                        user_interaction = '', 
                        vector_string = '', 
                        version = '', ), 
                    exploitability_score = 1.337, 
                    impact_score = 1.337, ),
                corrected_base_metric_v3 = vulncheck_sdk.models.api/base_metric_v3.api.BaseMetricV3(
                    cvss_v3 = vulncheck_sdk.models.api/cvssv3.api.CVSSV3(
                        attack_complexity = '', 
                        attack_vector = '', 
                        availability_impact = '', 
                        base_score = 1.337, 
                        base_severity = '', 
                        confidentiality_impact = '', 
                        integrity_impact = '', 
                        privileges_required = '', 
                        scope = '', 
                        user_interaction = '', 
                        vector_string = '', 
                        version = '', ), 
                    exploitability_score = 1.337, 
                    impact_score = 1.337, ),
                epss = vulncheck_sdk.models.api/epss.api.EPSS(
                    epss_percentile = 1.337, 
                    epss_score = 1.337, 
                    last_modified = '', ),
                metric_v40 = vulncheck_sdk.models.advisory/cvssv40.advisory.CVSSV40(
                    automatable = '', 
                    recovery = '', 
                    safety = '', 
                    attack_complexity = '', 
                    attack_requirements = '', 
                    attack_vector = '', 
                    availability_requirement = '', 
                    base_score = 1.337, 
                    base_severity = '', 
                    confidentiality_requirement = '', 
                    exploit_maturity = '', 
                    integrity_requirement = '', 
                    modified_attack_complexity = '', 
                    modified_attack_requirements = '', 
                    modified_attack_vector = '', 
                    modified_privileges_required = '', 
                    modified_sub_availability_impact = '', 
                    modified_sub_confidentiality_impact = '', 
                    modified_sub_integrity_impact = '', 
                    modified_user_interaction = '', 
                    modified_vuln_availability_impact = '', 
                    modified_vuln_confidentiality_impact = '', 
                    modified_vuln_integrity_impact = '', 
                    privileges_required = '', 
                    provider_urgency = '', 
                    sub_availability_impact = '', 
                    sub_confidentiality_impact = '', 
                    sub_integrity_impact = '', 
                    user_interaction = '', 
                    value_density = '', 
                    vector_string = '', 
                    version = '', 
                    vuln_availability_impact = '', 
                    vuln_confidentiality_impact = '', 
                    vuln_integrity_impact = '', 
                    vulnerability_response_effort = '', ),
                ssvc = [
                    vulncheck_sdk.models.api/ssvc.api.SSVC(
                        automatable = '', 
                        exploitation = '', 
                        source = '', 
                        technical_impact = '', )
                    ],
                temporal_metric_v2 = vulncheck_sdk.models.api/temporal_metric_v2.api.TemporalMetricV2(
                    cvss_v2 = vulncheck_sdk.models.api/temporal_cvssv2.api.TemporalCVSSV2(
                        exploitability = '', 
                        remediation_level = '', 
                        report_confidence = '', 
                        temporal_score = 1.337, 
                        vector_string = '', 
                        version = '', ), ),
                temporal_metric_v3 = vulncheck_sdk.models.api/temporal_metric_v3.api.TemporalMetricV3(
                    cvss_v3 = vulncheck_sdk.models.api/temporal_cvssv3.api.TemporalCVSSV3(
                        exploit_code_maturity = '', 
                        remediation_level = '', 
                        report_confidence = '', 
                        temporal_score = 1.337, 
                        vector_string = '', 
                        version = '', ), ),
                temporal_v3_corrected = vulncheck_sdk.models.api/temporal_metric_v3.api.TemporalMetricV3(
                    cvss_v3 = vulncheck_sdk.models.api/temporal_cvssv3.api.TemporalCVSSV3(
                        exploit_code_maturity = '', 
                        remediation_level = '', 
                        report_confidence = '', 
                        temporal_score = 1.337, 
                        vector_string = '', 
                        version = '', ), ),
                threat_metric_v40 = vulncheck_sdk.models.advisory/cvssv40_threat.advisory.CVSSV40Threat(
                    base_threat_score = 1.337, 
                    base_threat_severity = '', 
                    exploit_maturity = '', )
            )
        else:
            return ApiImpactExtended(
        )
        """

    def testApiImpactExtended(self):
        """Test ApiImpactExtended"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
