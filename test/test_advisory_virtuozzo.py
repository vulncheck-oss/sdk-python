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

from vulncheck_sdk.models.advisory_virtuozzo import AdvisoryVirtuozzo

class TestAdvisoryVirtuozzo(unittest.TestCase):
    """AdvisoryVirtuozzo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryVirtuozzo:
        """Test AdvisoryVirtuozzo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryVirtuozzo`
        """
        model = AdvisoryVirtuozzo()
        if include_optional:
            return AdvisoryVirtuozzo(
                affected = [
                    ''
                    ],
                cve = [
                    ''
                    ],
                date_added = '',
                fixed = [
                    ''
                    ],
                id = '',
                references = [
                    ''
                    ],
                title = '',
                url = ''
            )
        else:
            return AdvisoryVirtuozzo(
        )
        """

    def testAdvisoryVirtuozzo(self):
        """Test AdvisoryVirtuozzo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
