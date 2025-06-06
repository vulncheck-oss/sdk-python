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

from vulncheck_sdk.models.advisory_rustsec_advisory import AdvisoryRustsecAdvisory

class TestAdvisoryRustsecAdvisory(unittest.TestCase):
    """AdvisoryRustsecAdvisory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryRustsecAdvisory:
        """Test AdvisoryRustsecAdvisory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryRustsecAdvisory`
        """
        model = AdvisoryRustsecAdvisory()
        if include_optional:
            return AdvisoryRustsecAdvisory(
                advisory = vulncheck_sdk.models.advisory/rustsec_front_matter_advisory.advisory.RustsecFrontMatterAdvisory(
                    aliases = [
                        ''
                        ], 
                    categories = [
                        ''
                        ], 
                    cvss = '', 
                    date = '', 
                    informational = '', 
                    keywords = [
                        ''
                        ], 
                    package = '', 
                    references = [
                        ''
                        ], 
                    related = [
                        ''
                        ], 
                    rustsec_id = '', 
                    url = '', 
                    withdrawn = '', ),
                affected = vulncheck_sdk.models.advisory/rustsec_affected.advisory.RustsecAffected(
                    arch = [
                        ''
                        ], 
                    functions = '', 
                    os = [
                        ''
                        ], ),
                cve = [
                    ''
                    ],
                date_added = '',
                description = '',
                versions = vulncheck_sdk.models.advisory/rustsec_front_matter_versions.advisory.RustsecFrontMatterVersions(
                    patched = [
                        ''
                        ], 
                    unaffected = [
                        ''
                        ], )
            )
        else:
            return AdvisoryRustsecAdvisory(
        )
        """

    def testAdvisoryRustsecAdvisory(self):
        """Test AdvisoryRustsecAdvisory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
