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

from vulncheck_sdk.models.advisory_qualys_qid import AdvisoryQualysQID

class TestAdvisoryQualysQID(unittest.TestCase):
    """AdvisoryQualysQID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryQualysQID:
        """Test AdvisoryQualysQID
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryQualysQID`
        """
        model = AdvisoryQualysQID()
        if include_optional:
            return AdvisoryQualysQID(
                consequence = '',
                cve = [
                    ''
                    ],
                cvss_v2 = [
                    vulncheck_sdk.models.advisory/cvsss_v2_3.advisory.CvsssV2_3(
                        basescore = '', 
                        temporalscore = '', )
                    ],
                cvss_v3 = [
                    vulncheck_sdk.models.advisory/cvsss_v2_3.advisory.CvsssV2_3(
                        basescore = '', 
                        temporalscore = '', )
                    ],
                date_added = '',
                date_insert = '',
                description = '',
                patches = [
                    vulncheck_sdk.models.advisory/patch.advisory.Patch(
                        advisory_id = '', 
                        component = '', 
                        link = '', 
                        os_sw = '', )
                    ],
                published = '',
                qid = '',
                severity = '',
                solution = '',
                title = '',
                url = '',
                vendor_refs = [
                    vulncheck_sdk.models.advisory/vendor_ref.advisory.VendorRef(
                        vendor_ref = '', 
                        vendor_ref_url = '', )
                    ]
            )
        else:
            return AdvisoryQualysQID(
        )
        """

    def testAdvisoryQualysQID(self):
        """Test AdvisoryQualysQID"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
