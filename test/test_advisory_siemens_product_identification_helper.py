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

from vulncheck_sdk.models.advisory_siemens_product_identification_helper import AdvisorySiemensProductIdentificationHelper

class TestAdvisorySiemensProductIdentificationHelper(unittest.TestCase):
    """AdvisorySiemensProductIdentificationHelper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisorySiemensProductIdentificationHelper:
        """Test AdvisorySiemensProductIdentificationHelper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisorySiemensProductIdentificationHelper`
        """
        model = AdvisorySiemensProductIdentificationHelper()
        if include_optional:
            return AdvisorySiemensProductIdentificationHelper(
                model_numbers = [
                    ''
                    ]
            )
        else:
            return AdvisorySiemensProductIdentificationHelper(
        )
        """

    def testAdvisorySiemensProductIdentificationHelper(self):
        """Test AdvisorySiemensProductIdentificationHelper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
