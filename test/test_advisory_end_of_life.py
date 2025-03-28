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

from vulncheck_sdk.models.advisory_end_of_life import AdvisoryEndOfLife

class TestAdvisoryEndOfLife(unittest.TestCase):
    """AdvisoryEndOfLife unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryEndOfLife:
        """Test AdvisoryEndOfLife
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryEndOfLife`
        """
        model = AdvisoryEndOfLife()
        if include_optional:
            return AdvisoryEndOfLife(
                cve = [
                    ''
                    ],
                cycles = [
                    vulncheck_sdk.models.advisory/cycle.advisory.Cycle(
                        codename = '', 
                        cycle = '', 
                        discontinued = vulncheck_sdk.models.discontinued.discontinued(), 
                        eol = vulncheck_sdk.models.eol.eol(), 
                        extended_support = vulncheck_sdk.models.extended_support.extendedSupport(), 
                        latest = '', 
                        latest_release_date = '', 
                        link = '', 
                        lts = vulncheck_sdk.models.lts.lts(), 
                        release_date = '', 
                        release_label = '', 
                        support = vulncheck_sdk.models.support.support(), )
                    ],
                date_added = '',
                name = '',
                url = ''
            )
        else:
            return AdvisoryEndOfLife(
        )
        """

    def testAdvisoryEndOfLife(self):
        """Test AdvisoryEndOfLife"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
