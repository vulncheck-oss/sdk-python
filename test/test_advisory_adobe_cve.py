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

from vulncheck_sdk.models.advisory_adobe_cve import AdvisoryAdobeCVE

class TestAdvisoryAdobeCVE(unittest.TestCase):
    """AdvisoryAdobeCVE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryAdobeCVE:
        """Test AdvisoryAdobeCVE
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryAdobeCVE`
        """
        model = AdvisoryAdobeCVE()
        if include_optional:
            return AdvisoryAdobeCVE(
                cve = '',
                cvss_score = '',
                cvss_vector = ''
            )
        else:
            return AdvisoryAdobeCVE(
        )
        """

    def testAdvisoryAdobeCVE(self):
        """Test AdvisoryAdobeCVE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
