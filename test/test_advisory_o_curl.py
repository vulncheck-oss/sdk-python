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

from vulncheck_sdk.models.advisory_o_curl import AdvisoryOCurl

class TestAdvisoryOCurl(unittest.TestCase):
    """AdvisoryOCurl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryOCurl:
        """Test AdvisoryOCurl
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryOCurl`
        """
        model = AdvisoryOCurl()
        if include_optional:
            return AdvisoryOCurl(
                affected = [
                    vulncheck_sdk.models.advisory/curl_affected.advisory.CurlAffected(
                        ranges = [
                            vulncheck_sdk.models.advisory/curl_range.advisory.CurlRange(
                                events = [
                                    {
                                        'key' : ''
                                        }
                                    ], 
                                repo = '', 
                                type = '', )
                            ], 
                        versions = [
                            ''
                            ], )
                    ],
                aliases = [
                    ''
                    ],
                credits = [
                    vulncheck_sdk.models.advisory/curl_credit.advisory.CurlCredit(
                        name = '', 
                        type = '', )
                    ],
                database_specific = vulncheck_sdk.models.advisory/db_specific.advisory.DBSpecific(
                    cwe = vulncheck_sdk.models.advisory/curl_cwe.advisory.CurlCWE(
                        desc = '', 
                        id = '', ), 
                    award = vulncheck_sdk.models.advisory/award.advisory.Award(
                        amount = '', 
                        currency = '', ), 
                    last_affected = '', 
                    package = '', 
                    severity = '', 
                    url = '', 
                    www = '', ),
                details = '',
                id = '',
                modified = '',
                published = '',
                schema_version = '',
                summary = ''
            )
        else:
            return AdvisoryOCurl(
        )
        """

    def testAdvisoryOCurl(self):
        """Test AdvisoryOCurl"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
