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

from vulncheck_sdk.models.advisory_affected_ubuntu_package import AdvisoryAffectedUbuntuPackage

class TestAdvisoryAffectedUbuntuPackage(unittest.TestCase):
    """AdvisoryAffectedUbuntuPackage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryAffectedUbuntuPackage:
        """Test AdvisoryAffectedUbuntuPackage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryAffectedUbuntuPackage`
        """
        model = AdvisoryAffectedUbuntuPackage()
        if include_optional:
            return AdvisoryAffectedUbuntuPackage(
                break_commit_url = [
                    ''
                    ],
                fix_commit_url = [
                    ''
                    ],
                package_name = '',
                package_release_status = [
                    vulncheck_sdk.models.advisory/ubuntu_package_release_status.advisory.UbuntuPackageReleaseStatus(
                        affected = True, 
                        fixed = True, 
                        fixed_version = '', 
                        lts = True, 
                        release = '', 
                        release_long = '', 
                        release_version = '', 
                        status = '', )
                    ],
                upstream_fix_url = [
                    ''
                    ]
            )
        else:
            return AdvisoryAffectedUbuntuPackage(
        )
        """

    def testAdvisoryAffectedUbuntuPackage(self):
        """Test AdvisoryAffectedUbuntuPackage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
