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

from vulncheck_sdk.models.advisory_range import AdvisoryRange

class TestAdvisoryRange(unittest.TestCase):
    """AdvisoryRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryRange:
        """Test AdvisoryRange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryRange`
        """
        model = AdvisoryRange()
        if include_optional:
            return AdvisoryRange(
                events = [
                    vulncheck_sdk.models.advisory/event.advisory.Event(
                        fixed = '', 
                        introduced = '', 
                        last_affected = '', 
                        limit = '', )
                    ],
                repo = '',
                type = ''
            )
        else:
            return AdvisoryRange(
        )
        """

    def testAdvisoryRange(self):
        """Test AdvisoryRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
