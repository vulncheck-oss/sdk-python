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

from vulncheck_sdk.models.advisory_aus_cert import AdvisoryAusCert

class TestAdvisoryAusCert(unittest.TestCase):
    """AdvisoryAusCert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryAusCert:
        """Test AdvisoryAusCert
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryAusCert`
        """
        model = AdvisoryAusCert()
        if include_optional:
            return AdvisoryAusCert(
                body = '',
                bulletin_id = '',
                cve = [
                    ''
                    ],
                cvss = '',
                date_added = '',
                link = '',
                operating_system = '',
                product = '',
                publisher = '',
                resolution = ''
            )
        else:
            return AdvisoryAusCert(
        )
        """

    def testAdvisoryAusCert(self):
        """Test AdvisoryAusCert"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
