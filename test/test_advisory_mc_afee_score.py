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

from vulncheck_sdk.models.advisory_mc_afee_score import AdvisoryMcAfeeScore

class TestAdvisoryMcAfeeScore(unittest.TestCase):
    """AdvisoryMcAfeeScore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryMcAfeeScore:
        """Test AdvisoryMcAfeeScore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryMcAfeeScore`
        """
        model = AdvisoryMcAfeeScore()
        if include_optional:
            return AdvisoryMcAfeeScore(
                base = '',
                cve = '',
                temporal = '',
                vector = ''
            )
        else:
            return AdvisoryMcAfeeScore(
        )
        """

    def testAdvisoryMcAfeeScore(self):
        """Test AdvisoryMcAfeeScore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
