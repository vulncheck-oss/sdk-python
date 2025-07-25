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

from vulncheck_sdk.models.advisory_metric import AdvisoryMetric

class TestAdvisoryMetric(unittest.TestCase):
    """AdvisoryMetric unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryMetric:
        """Test AdvisoryMetric
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryMetric`
        """
        model = AdvisoryMetric()
        if include_optional:
            return AdvisoryMetric(
                cvss_v2_0 = vulncheck_sdk.models.advisory/m_cvss_v20.advisory.MCvssV20(
                    access_vector = '', 
                    attack_complexity = '', 
                    authentication = '', 
                    availability_impact = '', 
                    base_score = 1.337, 
                    confidentiality_impact = '', 
                    integrity_impact = '', 
                    vector_string = '', 
                    version = '', ),
                cvss_v3_0 = vulncheck_sdk.models.advisory/m_cvss_v30.advisory.MCvssV30(
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
                cvss_v3_1 = vulncheck_sdk.models.advisory/m_cvss_v31.advisory.MCvssV31(
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
                cvss_v4_0 = vulncheck_sdk.models.advisory/m_cvss_v40.advisory.MCvssV40(
                    automatable = '', 
                    recovery = '', 
                    safety = '', 
                    attack_complexity = '', 
                    attack_requirements = '', 
                    attack_vector = '', 
                    base_score = 1.337, 
                    base_severity = '', 
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
                format = '',
                other = vulncheck_sdk.models.advisory/metrics_other.advisory.MetricsOther(
                    content = '', 
                    type = '', )
            )
        else:
            return AdvisoryMetric(
        )
        """

    def testAdvisoryMetric(self):
        """Test AdvisoryMetric"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
