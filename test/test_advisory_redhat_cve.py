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

from vulncheck_sdk.models.advisory_redhat_cve import AdvisoryRedhatCVE

class TestAdvisoryRedhatCVE(unittest.TestCase):
    """AdvisoryRedhatCVE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryRedhatCVE:
        """Test AdvisoryRedhatCVE
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryRedhatCVE`
        """
        model = AdvisoryRedhatCVE()
        if include_optional:
            return AdvisoryRedhatCVE(
                advisories = [
                    ''
                    ],
                advisory_csaf_vex_url = [
                    ''
                    ],
                affected_packages = [
                    ''
                    ],
                affected_release = [
                    vulncheck_sdk.models.advisory/affected_rel.advisory.AffectedRel(
                        advisory = '', 
                        cpe = '', 
                        package = '', 
                        product_name = '', 
                        release_date = '', )
                    ],
                bugzilla = '',
                bugzilla_description = '',
                cve = [
                    ''
                    ],
                cve_csaf_vex_url = '',
                cvss3_score = '',
                cvss3_scoring_vector = '',
                cvss_score = 1.337,
                cvss_scoring_vector = '',
                cwe = '',
                package_state = [
                    vulncheck_sdk.models.advisory/package_stat.advisory.PackageStat(
                        cpe = '', 
                        fix_state = '', 
                        package_name = '', 
                        product_name = '', )
                    ],
                packages = [
                    vulncheck_sdk.models.advisory/vuln_check_package.advisory.VulnCheckPackage(
                        arch = '', 
                        distro = '', 
                        filename = '', 
                        md5 = '', 
                        name = '', 
                        purl = '', 
                        version = '', )
                    ],
                public_date = '',
                resource_url = '',
                severity = ''
            )
        else:
            return AdvisoryRedhatCVE(
        )
        """

    def testAdvisoryRedhatCVE(self):
        """Test AdvisoryRedhatCVE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
