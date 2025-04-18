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

from vulncheck_sdk.models.advisory_amazon_cve import AdvisoryAmazonCVE

class TestAdvisoryAmazonCVE(unittest.TestCase):
    """AdvisoryAmazonCVE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryAmazonCVE:
        """Test AdvisoryAmazonCVE
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryAmazonCVE`
        """
        model = AdvisoryAmazonCVE()
        if include_optional:
            return AdvisoryAmazonCVE(
                affected = [
                    vulncheck_sdk.models.advisory/amazon_affected_package.advisory.AmazonAffectedPackage(
                        advisory = '', 
                        package = '', 
                        platform = '', 
                        release_date = '', 
                        status = '', )
                    ],
                cve = [
                    ''
                    ],
                cvss_score = '',
                cvss_vector = '',
                date_added = '',
                references = [
                    ''
                    ],
                summary = '',
                title = '',
                updated_at = '',
                url = ''
            )
        else:
            return AdvisoryAmazonCVE(
        )
        """

    def testAdvisoryAmazonCVE(self):
        """Test AdvisoryAmazonCVE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
