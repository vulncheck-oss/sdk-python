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

from vulncheck_sdk.models.advisory_m_identification import AdvisoryMIdentification

class TestAdvisoryMIdentification(unittest.TestCase):
    """AdvisoryMIdentification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryMIdentification:
        """Test AdvisoryMIdentification
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryMIdentification`
        """
        model = AdvisoryMIdentification()
        if include_optional:
            return AdvisoryMIdentification(
                alias = vulncheck_sdk.models.advisory/i_val.advisory.IVal(
                    value = '', ),
                id = vulncheck_sdk.models.advisory/i_val.advisory.IVal(
                    value = '', )
            )
        else:
            return AdvisoryMIdentification(
        )
        """

    def testAdvisoryMIdentification(self):
        """Test AdvisoryMIdentification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
