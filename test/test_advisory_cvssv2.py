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

from vulncheck_sdk.models.advisory_cvssv2 import AdvisoryCVSSV2

class TestAdvisoryCVSSV2(unittest.TestCase):
    """AdvisoryCVSSV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryCVSSV2:
        """Test AdvisoryCVSSV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryCVSSV2`
        """
        model = AdvisoryCVSSV2()
        if include_optional:
            return AdvisoryCVSSV2(
                access_complexity = '',
                access_vector = '',
                authentication = '',
                availability_impact = '',
                availability_requirement = '',
                base_score = 1.337,
                collateral_damage_potential = '',
                confidentiality_impact = '',
                confidentiality_requirement = '',
                environmental_score = 1.337,
                exploitability = '',
                integrity_impact = '',
                integrity_requirement = '',
                remediation_level = '',
                report_confidence = '',
                target_distribution = '',
                temporal_score = 1.337
            )
        else:
            return AdvisoryCVSSV2(
        )
        """

    def testAdvisoryCVSSV2(self):
        """Test AdvisoryCVSSV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
