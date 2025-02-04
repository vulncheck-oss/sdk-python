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

from vulncheck_sdk.models.advisory_eol_release_data import AdvisoryEOLReleaseData

class TestAdvisoryEOLReleaseData(unittest.TestCase):
    """AdvisoryEOLReleaseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryEOLReleaseData:
        """Test AdvisoryEOLReleaseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryEOLReleaseData`
        """
        model = AdvisoryEOLReleaseData()
        if include_optional:
            return AdvisoryEOLReleaseData(
                already_eol = True,
                branch = '',
                branch_url = '',
                codename = '',
                cpe = '',
                eol_date = '',
                eol_date_extended_support = '',
                eol_date_premier_support = '',
                eol_elts_date = '',
                eol_lts_date = '',
                git_branch = '',
                git_branch_url = '',
                lts = True,
                minor_releases = [
                    ''
                    ],
                product = '',
                release_date = '',
                release_name = '',
                source_url = '',
                technology_level = '',
                vendor = '',
                version = '',
                version_api = '',
                version_darwin = '',
                version_sunos = '',
                windows_current_build = '',
                windows_display_version = '',
                windows_edition_id = '',
                windows_insider_preview = True
            )
        else:
            return AdvisoryEOLReleaseData(
        )
        """

    def testAdvisoryEOLReleaseData(self):
        """Test AdvisoryEOLReleaseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
