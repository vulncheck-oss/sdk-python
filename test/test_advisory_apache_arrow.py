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

from vulncheck_sdk.models.advisory_apache_arrow import AdvisoryApacheArrow

class TestAdvisoryApacheArrow(unittest.TestCase):
    """AdvisoryApacheArrow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryApacheArrow:
        """Test AdvisoryApacheArrow
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryApacheArrow`
        """
        model = AdvisoryApacheArrow()
        if include_optional:
            return AdvisoryApacheArrow(
                cve = [
                    ''
                    ],
                date_added = '',
                summary = '',
                title = '',
                url = ''
            )
        else:
            return AdvisoryApacheArrow(
        )
        """

    def testAdvisoryApacheArrow(self):
        """Test AdvisoryApacheArrow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
