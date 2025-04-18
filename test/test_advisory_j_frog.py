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

from vulncheck_sdk.models.advisory_j_frog import AdvisoryJFrog

class TestAdvisoryJFrog(unittest.TestCase):
    """AdvisoryJFrog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryJFrog:
        """Test AdvisoryJFrog
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryJFrog`
        """
        model = AdvisoryJFrog()
        if include_optional:
            return AdvisoryJFrog(
                cpes = [
                    vulncheck_sdk.models.advisory/nvd20_cvecpe_match.advisory.NVD20CVECPEMatch(
                        criteria = '', 
                        match_criteria_id = '', 
                        version_end_excluding = '', 
                        version_end_including = '', 
                        version_start_excluding = '', 
                        version_start_including = '', 
                        vulnerable = True, )
                    ],
                cve = [
                    ''
                    ],
                date_added = '',
                product = '',
                severity = '',
                summary = '',
                url = '',
                versions = [
                    ''
                    ]
            )
        else:
            return AdvisoryJFrog(
        )
        """

    def testAdvisoryJFrog(self):
        """Test AdvisoryJFrog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
